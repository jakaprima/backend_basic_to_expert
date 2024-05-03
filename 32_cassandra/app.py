from flask import Flask, jsonify, request
from cassandra_connection import get_connection

app = Flask(__name__)

@app.route('/data/<key>', methods=['GET'])
def get_data(key):
    session = get_connection()
    # Write CQL statement to fetch data based on key
    rows = session.execute("SELECT * FROM your_table WHERE key = ?", (key,))
    data = []
    for row in rows:
        # Process row data and convert to dictionary
        data.append({'column1': row.column1, 'column2': row.column2})
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
