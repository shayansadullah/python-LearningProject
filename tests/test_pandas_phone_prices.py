"""Demonstrates how to read a CSV file containing phone prices into a pandas DataFrame and print its contents."""  # noqa: E501

import pandas as pd

df_phone_prices = pd.read_csv("data/mobile-phone-data.csv")
print(f"DataFrame from CSV:\n{df_phone_prices}")
print(f"Length of DataFrame: {len(df_phone_prices)}")
print(f"DataFrame first 5 rows:\n{df_phone_prices.head()}")
print(f"DataFrame last 5 rows:\n{df_phone_prices.tail()}")
print(f"DataFrame first 10 rows:\n{df_phone_prices.head(10)}")

specific_columns = df_phone_prices[["battery_power", "touch_screen"]]

print(f"DataFrame show specific columns:\n{specific_columns}")
print(
    f"DataFrame shows specific rows and columns filter:\n{df_phone_prices.iloc[0:22, 0:4]}"
)

filtered_phones = (
    df_phone_prices[df_phone_prices["clock_speed"] >= 2.4].head(22).iloc[:, 0:4]
)
print(
    f"DataFrame shows specific rows and columns filter with condition:\n{filtered_phones}"
)

print(f"DataFrame show describe:\n{df_phone_prices.describe()}\n")
print(f"DataFrame show correlation:\n{df_phone_prices.corr()}\n")

