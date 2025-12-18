# client/upstox_client.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class UpstoxClient:
    def __init__(self):
        self.base_url = "https://api.upstox.com/v2"

        access_token = os.getenv("UPSTOX_ACCESS_TOKEN")
        if not access_token:
            raise Exception("UPSTOX_ACCESS_TOKEN not found. Run OAuth first.")

        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json"
        }

    def _get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 401:
            raise Exception("Access token expired. Re-run OAuth.")

        if response.status_code != 200:
            raise Exception(f"API error {response.status_code}: {response.text}")

        return response.json()

    # -------- REAL API METHODS --------

    def get_profile(self):
        return self._get("/user/profile")

    def get_funds_and_margin(self):
        return self._get("/user/funds")

    def get_holdings(self):
        return self._get("/portfolio/holdings")