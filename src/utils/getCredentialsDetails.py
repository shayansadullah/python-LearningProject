import json
import os


class CredentialsReader:
    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'credentials.json')

    def get_cretdetials_details(self):
        """Read credentials from credentials.json file"""
        with open(self.data_path, 'r') as file:
            data = json.load(file)
        return data['user_credentials']
