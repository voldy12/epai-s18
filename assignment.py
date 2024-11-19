class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume


from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock(
            "TSLA",
            date(2018, 11, 22),
            Decimal("338.19"),
            Decimal("338.64"),
            Decimal("337.60"),
            Decimal("338.19"),
            365_607,
        ),
        Stock(
            "AAPL",
            date(2018, 11, 22),
            Decimal("176.66"),
            Decimal("177.25"),
            Decimal("176.64"),
            Decimal("176.78"),
            3_699_184,
        ),
        Stock(
            "MSFT",
            date(2018, 11, 22),
            Decimal("103.25"),
            Decimal("103.48"),
            Decimal("103.07"),
            Decimal("103.11"),
            4_493_689,
        ),
    ],
    "trades": [
        Trade(
            "TSLA",
            datetime(2018, 11, 22, 10, 5, 12),
            "buy",
            Decimal("338.25"),
            100,
            Decimal("9.99"),
        ),
        Trade(
            "AAPL",
            datetime(2018, 11, 22, 10, 30, 5),
            "sell",
            Decimal("177.01"),
            20,
            Decimal("9.99"),
        ),
    ],
}

import json
class CustomEncoder(json.JSONEncoder):
    def default(self, obj: Stock | Trade) -> dict:
        
        if isinstance(obj, Stock):
            stock = Stock(
                
                    date = obj.date.isoformat(),
                    open_ = str(obj.open),
                    close = str(obj.close),
                    high = str(obj.high),
                    low = str(obj.low),
                    symbol = obj.symbol,
                    volume= obj.volume,
            ).__dict__
            stock.update(type = 'Stock')
            return stock
        elif isinstance(obj, Trade):
            trade = Trade(
                timestamp = obj.timestamp.isoformat(),
                symbol = obj.symbol,
                order = obj.order,
                price = str(obj.price),
                volume = obj.volume,
                commission = str(obj.commission),
            ).__dict__
            trade.update(type = 'Trade')
            return trade

def custom_decoder(obj: dict) -> Stock | Trade:
    if isinstance(obj, dict):
        if 'type' in obj:
            return deserialize_dict(obj)

        else:
            return obj
    else:
        raise ValueError(f"Unknown type: {type(obj)}")
    
def deserialize_dict(obj: dict) -> Stock | Trade:
    if obj['type'] == 'Stock':
        del obj['type']
        return Stock(date = date.fromisoformat(obj['date']),
                    open_ = Decimal(obj['open']),
                    close = Decimal(obj['close']),
                    high = Decimal(obj['high']),
                    low = Decimal(obj['low']),
                    symbol = obj['symbol'],
                    volume= obj['volume'],
                    )
    elif obj['type'] == 'Trade':
        del obj['type']
        return Trade(timestamp = datetime.fromisoformat(obj['timestamp']),
                     price = Decimal(obj['price']),
                     commission = Decimal(obj['commission']),
                     volume = obj['volume'],
                     symbol = obj['symbol'],
                     order = obj['order'],
                     )
    else:
        raise ValueError(f"Unknown type: {type(obj)}")
    
from marshmallow import Schema, fields

class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal()
    close = fields.Decimal()
    high = fields.Decimal()
    low = fields.Decimal()
    volume = fields.Int()

    def load(self, data: dict) -> Stock:
        data['open_'] = data.pop('open')
        return Stock(**data)        



class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal()
    volume = fields.Int()
    commission = fields.Decimal()

    def load(self, data: dict) -> Trade:
        return Trade(**data)

def serialize_with_marshmallow(obj: Stock | Trade) -> str:
    if isinstance(obj, Stock):
        stock_dict =  StockSchema().dump(obj)
        return json.dumps(stock_dict, cls=CustomEncoder)
    elif isinstance(obj, Trade):
        trade_dict = TradeSchema().dump(obj)
        return json.dumps(trade_dict, cls=CustomEncoder)
    else:
        raise ValueError(f"Unknown type: {type(obj)}")

def deserialize_with_marshmallow(json_str: str, schema: Schema) -> Stock | Trade:
    data = json.loads(json_str)
    return schema.load(data)
