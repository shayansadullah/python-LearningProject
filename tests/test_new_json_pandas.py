"""Test for reading JSON data using pandas."""

import json

import pandas as pd


def test_json_pandas():
    """Test reading JSON data using pandas."""
    json_file_path = "data/example-1.json"

    with open(json_file_path) as f:
        json_data = f.read()
        print("JSON Data:", json_data)


def test_to_object_to_json_conversion():
    """Test conversion of JSON data to Python objects and back to JSON."""
    json_file_path = "data/example-1.json"
    df_from_json = pd.read_json(json_file_path)
    print(f"This is to json:\n {df_from_json}")
    json_string = df_from_json.to_json()
    print(json_string)
