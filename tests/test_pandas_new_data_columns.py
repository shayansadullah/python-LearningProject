"""Test for reading JSON data using pandas."""

import pandas as pd

from src.utils import pandasHelper as ph


def test_read_json_helper():
    """Read the JSON file."""
    json_file_path = "data/example-4.json"
    json_df = ph.PandasHelper.read_json_helper(json_file_path)
    print("JSON Data:", json_df)
    df_one = pd.DataFrame(json_df[0])
    df_two = pd.DataFrame(json_df[1])
    df_three = pd.DataFrame(json_df[2])
    df_combined = pd.concat([df_one, df_two])
    df_combined = pd.concat([df_combined, df_three], axis=0)
    df_combined.reset_index(drop=True, inplace=True)
    print(df_combined)
