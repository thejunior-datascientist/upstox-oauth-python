from flask import Flask, request
from oauth.oauth_flow import exchange_code_for_token

app = Flask(__name__)

@app.route("/callback")

def callback():
    print("CALLBACK ENTERED", flush=True)
    code = request.args.get("code")

    if not code:
        return "No code received", 400

    token_data = exchange_code_for_token(code)

    return "OAuth successful. Access token stored. You can close this tab."

if __name__ == "__main__":
    app.run(port=8000)