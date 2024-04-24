"""
The after_request function is another decorator that adds the HSTS header to every response sent from the server.
 The HSTS header instructs the browser to only use HTTPS for future requests for the specified duration (max-age), 
 which in this case is set to 1 year (31536000 seconds). Additionally, the includeSubDomains directive ensures that 
 the HSTS policy applies to all subdomains of your site.
"""

from flask import Flask, redirect

app = Flask(__name__)

# Route to redirect HTTP requests to HTTPS
@app.route('/')
def index():
    return 'Hello, world!'

# Redirect HTTP requests to HTTPS
@app.before_request
def before_request():
    if not request.is_secure:
        return redirect(request.url.replace('http://', 'https://'), code=301)

# Add HSTS header to responses
@app.after_request
def after_request(response):
    # Set HSTS header with a max-age of 1 year (in seconds) and includeSubDomains directive
    response.headers.add('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
    return response

if __name__ == '__main__':
    app.run(debug=True)


