# Stock and Trade Data Serialization

![Python Tests](https://github.com/voldy12/epai-s18/actions/workflows/python-tests.yml/badge.svg)

## 🚀 Overview

This project demonstrates advanced JSON serialization and deserialization techniques in Python, specifically handling financial data structures like Stock and Trade objects. It implements both custom JSON encoding/decoding and Marshmallow schema-based serialization.

## 🎯 Features

- Custom JSON serialization for Stock and Trade objects
- Custom JSON deserialization with type preservation
- Marshmallow schema-based serialization alternative
- Comprehensive test suite
- Support for complex data types (Decimal, DateTime)
- Automated testing with GitHub Actions

## 🏗️ Project Structure     

- `assignment.py` - Main implementation
- `test_assignment.py` - Test suite  
- `.github/workflows` - GitHub Actions configuration
- `README.md` - This file

## 📋 Prerequisites         

- Python 3.12
- pip (Python package installer)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/{username}/{repository}.git
cd {repository}
```


2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Stock and Trade Classes

```python
from datetime import date, datetime
from decimal import Decimal
# Create a Stock instance
stock = Stock('TSLA',
date(2018, 11, 22),
Decimal('338.19'),
Decimal('338.64'),
Decimal('337.60'),
Decimal('338.19'),
365_607)

#Create a Trade instance
trade = Trade('TSLA',
datetime(2018, 11, 22, 10, 5, 12),
'buy',
Decimal('338.25'),
100,
Decimal('9.99'))
```


## 🧪 Running Tests

Run the test suite using pytest:

bash
pytest test_assignment.py -v


## 🔄 CI/CD

This project uses GitHub Actions for continuous integration. The workflow:
- Runs on Python 3.12
- Executes on push to main and pull requests
- Runs the complete test suite
- Provides immediate feedback on code changes

## 📝 Assignment Details

The project implements three main exercises:
1. Custom JSON Encoder for serialization
2. Custom JSON Decoder for deserialization
3. Marshmallow-based serialization/deserialization

Each implementation handles:
- Date and DateTime objects
- Decimal numbers
- Nested data structures
- Type preservation during serialization/deserialization


## ✨ Acknowledgments

- Built as part of an advanced Python programming course
- Uses industry-standard libraries and best practices
- Implements real-world financial data handling patterns

---
