"""Tests for pandas operations with realistic data."""

import pandas as pd

car_brands = ["Brand", "Model", "Year", "Price", "Transmission"]

pd.DataFrame(columns=car_brands)

car_data = {
    "Brand": [
        "Toyota",
        "Honda",
        "Ford",
        "BNW",
        "Audi",
        "Mercedes",
        "Tesla",
        "Volkswagen",
        "Hyundai",
        "Kia",
    ],
    "Model": [
        "Camry",
        "Civic",
        "Mustang",
        "X5",
        "A4",
        "C-Class",
        "Model S",
        "Golf",
        "Elantra",
        "Sorento",
    ],
    "Year": [2020, 2019, 2021, 2022, 2023, 2021, 2022, 2020, 2019, 2021],
    "Price": [24000, 22000, 26000, 55000, 40000, 50000, 80000, 30000, 20000, 25000],
    "Transmission": [
        "Automatic",
        "Manual",
        "Automatic",
        "Automatic",
        "Manual",
        "Automatic",
        "Automatic",
        "Manual",
        "Automatic",
        "Manual",
    ],
}


car_sales_data_df = pd.DataFrame(car_data)
print(car_sales_data_df)
print(f"Number of rows in the DataFrame: {len(car_sales_data_df)}")
print(f"Last 2 rows:\n{car_sales_data_df.tail(2)}")
print(f"First 2 rows:\n{car_sales_data_df.head(2)}")

print(f"DataFrame columns:\n{car_sales_data_df[['Brand', 'Price']]}")

print(f"Dataframe rows:\n{car_sales_data_df.iloc[0:2, 0:1]}")

print(
    f"Dataframe filter rows:\n{car_sales_data_df[car_sales_data_df['Price'] > 30000]}"
)

car_sales_data_df.loc[
    car_sales_data_df["Transmission"] == "Automatic", "Transmission"
] = "Semi-Automatic"
print(f"Dataframe replace column values:\n{car_sales_data_df}")
