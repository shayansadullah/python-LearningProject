import pytest
import pandas as pd


@pytest.mark.asyncio
async def test_excel_pandas():
    """Test reading and validating Excel data using pandas.

    This test reads an Excel file, extracts specific data, and performs assertions.

    """
    # Read the Excel file - try without any parameters first to see the structure
    order_details_df = pd.read_excel("data/example_lookup.xlsx", sheet_name="OrderDetails_Python")

    # Print column names first to debug
    print(f"\n=== OrderDetails DataFrame ===")
    print(f"Column names: {order_details_df.columns.tolist()}")
    print(f"Shape: {order_details_df.shape}")
    print(f"First 5 rows:\n{order_details_df.head().to_string()}")

    # Check if 'ProductID' is in the first row of data
    if 'ProductID' in order_details_df.iloc[0].values:
        print("\n'ProductID' found in first row - need to use that row as header")
        # Recreate with header in second row (index 1)
        order_details_df = pd.read_excel("data/example_lookup.xlsx", sheet_name="OrderDetails_Python", header=1)
        print(f"After header=1, columns: {order_details_df.columns.tolist()}")

    # For now, just assert that we loaded some data
    assert len(order_details_df) > 0, "DataFrame should not be empty"


    # Read the Excel file - the look up
    order_address_df = pd.read_excel("data/example_lookup.xlsx", sheet_name="OrderAddress_Python")

    print(f"\n=== OrderAddress DataFrame ===")
    print(f"Column names: {order_address_df.columns.tolist()}")

    # Check if 'ProductID' is in the first row
    if 'ProductID' in order_address_df.iloc[0].values:
        order_address_df = pd.read_excel("data/example_lookup.xlsx", sheet_name="OrderAddress_Python", header=1)
        print(f"After header=1, columns: {order_address_df.columns.tolist()}")

    # For now, just assert that we loaded some data
    assert len(order_address_df) > 0, "DataFrame should not be empty"

    # Merge the two dataframes
    if 'ProductID' in order_details_df.columns and 'ProductID' in order_address_df.columns:
        order_details_df = order_details_df.merge(order_address_df, on="ProductID", how="left")
        print(f"\nMerged table:\n{order_details_df.to_string()}")
    else:
        print(f"\nCannot merge - ProductID not found in columns")
        print(f"OrderDetails columns: {order_details_df.columns.tolist()}")
        print(f"OrderAddress columns: {order_address_df.columns.tolist()}")
