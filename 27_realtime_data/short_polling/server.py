from flask import Flask, render_template, request
import time
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

data = None  # This will hold the data we want to send to the client


@app.route('/short_polling')
def short_polling():
    polling_interval = 2  # Polling interval in seconds

    while True:
        # Simulate data generation (replace with your data source)
        new_data = {'value': random.randint(1, 100), 'timestamp': time.time()}
        global data
        data = new_data

        # Wait for a short interval before sending the data
        time.sleep(polling_interval)
        return data, 200


def update_data(new_data):
    global data
    data = new_data


if __name__ == "__main__":
    app.run()
