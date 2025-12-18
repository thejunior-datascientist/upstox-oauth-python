# Upstox OAuth + Python Client

This repository demonstrates a clean, end-to-end implementation of:
- OAuth2 authentication with Upstox
- Secure handling of access tokens using environment variables
- A reusable Python client for calling Upstox REST APIs

The project is intentionally kept simple and explicit, focusing on raw HTTP requests
instead of hiding behavior behind SDK abstractions.

---

## Project Structure
oauth/      # OAuth flow (auth URL generation, callback server, token exchange)  
client/     # Reusable Upstox API client  
scripts/    # Example scripts using the client  

## Prerequisites

- Python 3.9+
- An Upstox developer account
- Upstox app with OAuth enabled
 
## Setup

### 1. Clone the repository
git clone <your-repo-url>
cd upstox_api

### 2. Create a virtual environment 
python -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Create .env file (not committed)
Create a file named .env in the project root:  

UPSTOX_CLIENT_ID=your_client_id  
UPSTOX_CLIENT_SECRET=your_client_secret  
UPSTOX_ACCESS_TOKEN=  

# OAuth Flow
Terminal 1 – Start callback server  
run: python -m oauth.callback

Terminal 2 – Generate auth URL  
run: python -m oauth.oauth_flow  
	1.	Open the printed URL in your browser  
	2.	Login to Upstox  
	3.	On success, the access token is written to .env  

