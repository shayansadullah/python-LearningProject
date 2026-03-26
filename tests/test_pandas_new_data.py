"""Test for reading JSON data using pandas."""

import pandas as pd

new_data = {
    "name": ["Example 1", "Example 2"],
    "description": [
        "This is an example JSON file.",
        "This is another example JSON file.",
    ],
    "version": ["1.0.0", "2.0.0"],
}

new_data2 = {
    "name": ["Example 3", "Example 4"],
    "description": [
        "This is yet another example JSON file.",
        "This is one more example JSON file.",
    ],
    "version": ["3.0.0", "4.0.0"],
}

column_data = {
    "third": [
        "Additional data 1",
        "Additional data 2",
    ]
}

df_one = pd.DataFrame(new_data)
df_two = pd.DataFrame(new_data2)
df_three = pd.DataFrame(column_data)
df_combined = pd.concat([df_one, df_two])
df_combined = pd.concat([df_combined, df_three], axis=0)
df_combined.reset_index(drop=True, inplace=True)
print(df_combined)
