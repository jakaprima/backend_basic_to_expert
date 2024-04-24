import time

from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def generate_data():
    while True:
        data = f"New data: {time.time()}"
        yield f"data: {data}\n\n"
        # simulasi delay
        time.sleep(2)


@app.route("/events")
def events():
    response = Response(generate_data(), mimetype="text/event-stream")
    print("RESPONSE", response)
    response.headers["Cache-Control"] = "no-cache"
    return response


if __name__ == "__main__":
    app.run()
