"""Helper utilities for pandas DataFrame operations."""

import pandas as pd


class PandasHelper:
    """Helper class for pandas operations."""

    @staticmethod
    def read_excel_helper(file_path, sheet_name, header=None):
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
    def output_dataframe_info(df, sheet_name):
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

