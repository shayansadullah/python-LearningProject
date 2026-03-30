"""Test for reading JSON data using pandas."""

import pandas as pd

from src.utils import pandasHelper as ph


def test_read_json_helper():
    """Read the JSON file."""
    json_file_path = "data/example-1.json"
    json_df = ph.PandasHelper.read_json_helper(json_file_path)
    print("JSON Data:", json_df)


def test_to_object_to_json_conversion2():
    """Test conversion of JSON data to Python objects and back to JSON."""
    json_file_path = "data/example-1.json"
    json_df = ph.PandasHelper.read_json_helper(json_file_path)
    json_string = pd.DataFrame(json_df).to_json()
    print(json_string)
