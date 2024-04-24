import os
from flask import Flask, redirect, request, session
from requests_oauthlib import OAuth2Session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# GitHub OAuth settings
client_id = '54ccea671ac9392e66b5'
client_secret = 'a37bf749a8e4efa0009b377a230cb1bcca1251f6'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

@app.route('/')
def index():
    return 'Hello, welcome to OAuth example!'

@app.route('/login')
def login():
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later verification.
    session['oauth_state'] = state
    return redirect(authorization_url)

@app.route('/callback', methods=['GET'])
def callback():
    if 'oauth_state' not in session:
        return 'Error: OAuth state not found in session'
    github = OAuth2Session(client_id, state=session['oauth_state'])
    token = github.fetch_token(
        token_url,
        authorization_response=request.url,
        client_secret=client_secret
    )

    # Example: Get user's information
    user_info = github.get('https://api.github.com/user').json()

    return f'Logged in as {user_info["login"]}'

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Specify file paths
    cert_file = os.path.join(current_directory, 'cert.pem')
    key_file = os.path.join(current_directory, 'key.pem')
    app.run(debug=True, ssl_context=(cert_file, key_file))
    # app.run(debug=True)
