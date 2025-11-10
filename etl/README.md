# ETL Scripts

This directory contains ETL (Extract, Transform, Load) scripts for processing data.

## Modules

- `extract.py` - Data extraction from various sources (CSV, JSON, databases)
- `transform.py` - Data transformation and cleaning operations
- `load.py` - Loading transformed data to target destinations

## Usage

```python
from etl import extract, transform, load

# Extract data
df = extract.extract_from_csv('data/source.csv')

# Transform data
df = transform.clean_data(df)
df = transform.normalize_columns(df, ['name', 'email'])

# Load data
load.load_to_csv(df, 'data/output.csv')
```

## Requirements

The ETL scripts require:
- pandas
- Additional dependencies based on data sources (SQLAlchemy for databases, etc.)
