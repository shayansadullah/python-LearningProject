import pandas as pd

class PandasHelper:
    """Helper class for pandas operations."""

    @staticmethod
    def read_excel(file_path, sheet_name, header=None):
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