import pandas as pd

car_brands = ["Brand", "Model", "Year", "Price"]

pd.DataFrame(columns=car_brands)

car_data = {
    "Brand": ["Toyota", "Honda", "Ford"],
    "Model": ["Camry", "Civic", "Mustang"],
    "Year": [2020, 2019, 2021],
}


car_sales_data_df = pd.DataFrame(car_data)
print(car_sales_data_df)
