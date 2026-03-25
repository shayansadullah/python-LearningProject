"""Test for reading JSON data using pandas."""

import pandas as pd

new_data = {
    "name": ["Example 1", "Example 2"],
    "description": ["This is an example JSON file.", "This is another example JSON file."],
    "version": ["1.0.0", "2.0.0"]
}

output = pd.DataFrame(new_data)
print(output)
