"""Test pandas Excel reading and merging functionality."""

import pytest

from src.utils import pandasHelper as ph


@pytest.mark.parametrize(
    "file_path, sheet1, sheet2, header",
    [
        ("data/example_lookup.xlsx", "OrderDetails_Python", "OrderAddress_Python", 0),
    ],
)
@pytest.mark.asyncio
async def test_excel_pandas(file_path, sheet1, sheet2, header):
    """Test reading and validating Excel data using pandas.

    This test reads an Excel file, extracts specific data, and performs assertions.

    """
    # Read first sheet
    order_details_df = ph.PandasHelper.read_excel_helper(
        file_path, sheet_name=sheet1, header=header
    )

    ph.PandasHelper.output_dataframe_info(order_details_df, sheet1)

    assert len(order_details_df) > 0, "DataFrame should not be empty"

    # Read second sheet
    order_address_df = ph.PandasHelper.read_excel_helper(
        file_path, sheet_name=sheet2, header=header
    )

    ph.PandasHelper.output_dataframe_info(order_address_df, sheet2)

    assert len(order_address_df) > 0, "DataFrame should not be empty"

    # Merge the two dataframes
    merged_df = order_details_df.merge(order_address_df, on="ProductID", how="left")
    ph.PandasHelper.output_dataframe_info(merged_df, "Merged DataFrame")


@pytest.mark.parametrize(
    "file_path, sheet1, header, expected_columns",
    [
        (
            "data/example_lookup.xlsx",
            "OrderDetails_Python",
            0,
            ["ProductID", "Name", "Price"],
        ),
        (
            "data/example_lookup.xlsx",
            "OrderAddress_Python",
            0,
            ["ProductID", "Address", "Tax Code"],
        ),
    ],
)
@pytest.mark.asyncio
async def test_excel_columns_match_expected_columns(
    file_path, sheet1, header, expected_columns
):
    """Test that the columns in the Excel sheets match expected columns."""  #
    # Read first sheet
    order_details_df = ph.PandasHelper.read_excel_helper(
        file_path, sheet_name=sheet1, header=header
    )

    assert ph.PandasHelper.check_columns(
        order_details_df, expected_columns
    ), f"Column mismatch in sheet '{sheet1}'"
