"""Utility for reading user credentials from JSON configuration file."""

import json
import os


class CredentialsReader:
    """Read and parse user credentials from credentials.json file."""

    """Read and parse user credentials from credentials.json file."""

    def __init__(self):
        """Initialize CredentialsReader with path to credentials.json."""
        self.data_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "data", "credentials.json"
        )

    def get_cretdetials_details(self):
        """Read credentials from credentials.json file."""
        with open(self.data_path) as file:
            data = json.load(file)
        return data["user_credentials"]
