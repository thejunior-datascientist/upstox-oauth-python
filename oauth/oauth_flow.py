from urllib.parse import urlencode
import os, requests
from dotenv import load_dotenv
from pathlib import Path

ENV_FILE = Path(__file__).resolve().parents[1] / ".env"
load_dotenv()



AUTH_URL = "https://api.upstox.com/v2/login/authorization/dialog"
TOKEN_URL = "https://api.upstox.com/v2/login/authorization/token"
REDIRECT_URI = "http://localhost:8000/callback"


def build_auth_url():
    params = {
        "response_type": "code",
        "client_id": os.getenv("UPSTOX_CLIENT_ID"),
        "redirect_uri": REDIRECT_URI,
    }
    return f"{AUTH_URL}?{urlencode(params)}"


def exchange_code_for_token(code: str):
    data = {
        "code": code,
        "client_id": os.getenv("UPSTOX_CLIENT_ID"),
        "client_secret": os.getenv("UPSTOX_CLIENT_SECRET"),
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    response = requests.post(TOKEN_URL, data=data)

    if response.status_code != 200:
        raise Exception(f"Token exchange failed: {response.text}")

    token_data = response.json()
    access_token = token_data["access_token"]

    existing_lines = []
    if ENV_FILE.exists():
        existing_lines = ENV_FILE.read_text().splitlines()

    new_lines = []
    token_written = False

    for line in existing_lines:
        if line.startswith("UPSTOX_ACCESS_TOKEN="):
            if not token_written:
                new_lines.append(f"UPSTOX_ACCESS_TOKEN={access_token}")
                token_written = True
        else:
            new_lines.append(line)

    if not token_written:
        new_lines.append(f"UPSTOX_ACCESS_TOKEN={access_token}")

    ENV_FILE.write_text("\n".join(new_lines) + "\n")

    return token_data

if __name__ == "__main__":
    print("Open this URL in browser:\n")
    print(build_auth_url())

