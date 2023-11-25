# USDA_STAT
A python library that uses API interface to obtain USDA/NASS Quick Stat data

---
## Introduction
provides a simplified interface to access data from the USDA's Quick Stats API. The library is designed to fetch agricultural data, process it, and return it in a user-friendly format.

## Installation

To use this library, you need Python installed on your machine. The library depends on `requests` and `pandas`and`usda_stat`, which can be installed using pip:

```bash
pip install requests pandas
```
```bash
pip install usda_stat
```

## Usage
Import the library into your Python script to start using its functionalities.

```python
import usda_quickstats
```

## Get API_KEY
First go to [USDA/NASS Quick Stats](https://quickstats.nass.usda.gov/api/) to get API_KEY
Then use KEY_init("your api key") to complete the configuration of API_KEY

## Functions

The library offers the following primary functions:

1. `get_data(params)`: Fetches specific data based on query parameters. Returns a pandas DataFrame.
2. `get_par(par)`: Returns possible values for a given column or header name in a DataFrame.
3. `get_counts(params)`: Retrieves the count of rows for queried data.

## Examples

### Fetching Data

```python
params = {"commodity_desc": "CORN", "year": 2020}
data = usda_quickstats.get_data(params)
print(data)
```

### Getting Parameter Values

```python
parameter_values = usda_quickstats.get_par("commodity_desc")
print(parameter_values)
```

### Getting Counts

```python
params = {"commodity_desc": "CORN", "year": 2020}
count = usda_quickstats.get_counts(params)
print(f"Number of records: {count}")
```

## Related link
[API usage documentation](https://quickstats.nass.usda.gov/api/)
