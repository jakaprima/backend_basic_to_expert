from flask import Flask, render_template, request
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data = None  # This will hold the data we want to send to the client


@app.route('/long_polling')
def long_polling():
    timeout = 5  # Set the polling timeout in seconds
    last_poll_time = time.time()  # Track the last poll time

    while True:
        # Check if new data is available (replace with your data generation logic)
        if data is not None and data['timestamp'] > last_poll_time:
            return data, 200  # Send data and exit the loop
        else:
            time.sleep(1)  # Sleep for a short duration to avoid busy waiting
            if time.time() - last_poll_time > timeout:
                return '{}', 200  # Return empty response after timeout

    # Never reached (if data is always available before timeout)
    return '{}', 200


def update_data(new_data):
    global data
    data = new_data

if __name__ == "__main__":
    app.run()
