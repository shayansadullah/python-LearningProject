"""Helper utilities for pandas DataFrame operations."""

import json

import pandas as pd


class PandasHelper:
    """Helper class for pandas operations."""

    @staticmethod
    def read_excel_helper(file_path, sheet_name, header=None) -> pd.DataFrame | None:
        """Read an Excel file and return a DataFrame.

        Args:
            file_path: Path to the Excel file.
            sheet_name: Name of the sheet to read.
            header: Row number to use as column names (default is None).

        Returns:
            A pandas DataFrame containing the data from the specified sheet.

        """
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, header=header)
            return df
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return None

    @staticmethod
    def read_json_helper(file_path) -> pd.DataFrame | None:
        """Read a JSON file and return a DataFrame.

        Args:
            file_path: Path to the JSON file.

        Returns:
            A pandas DataFrame containing the data from the JSON file.

        """
        try:
            with open(file_path) as f:
                data = json.load(f)
            if isinstance(data, list):
                return data
            return pd.DataFrame(data)
        except Exception as e:
            print(f"Error reading JSON file: {e}")
            return None

    @staticmethod
    def output_dataframe_info(df, sheet_name) -> None:
        """Print basic information about the dataframe.

        Args:
            df: The DataFrame to analyze.
            sheet_name: Name of the sheet for display purposes.

        Returns:
            None

        """
        if df is not None:
            print(f"\n=== {sheet_name} DataFrame ===")
            print(f"Columns: {df.columns.tolist()}")
            print(f"Shape: {df.shape}")
            print(f"\n{df.to_string()}")

    @staticmethod
    def check_columns(df, expected_columns) -> bool:
        """Check if the DataFrame contains the expected columns.

        Args:
            df: The DataFrame to check.
            expected_columns: A list of expected column names.

        Returns:
            True if all expected columns are present, False otherwise.

        """
        if df is None:
            return False
        missing = [col for col in expected_columns if col not in df.columns]
        extra = [col for col in df.columns if col not in expected_columns]
        if missing or extra:
            if missing:
                print(f"Missing expected columns: {missing}")
            if extra:
                print(f"Unexpected extra columns: {extra}")
            return False
        return True
