"""Test for reading JSON data using pandas."""

import json
import pytest

def test_json_pandas():
    """Test reading JSON data using pandas."""
    json_file_path = "data/example-1.json"

    with open(json_file_path) as f:
        json_data = f.read()
        print("JSON Data:", json_data)
