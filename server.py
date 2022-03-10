from flask import Flask, request, jsonify
import json

from flaskext.mysql import MySQL

# from venue import server_connection
import venue

# connection=server_connection

app = Flask(__name__)


@app.route('/insertvenue', methods=['POST'])
def insertvenue():
    request_payload = request.json
    # request_payload = json.loads(request.json)
    venue_id = venue.insert_venue(request_payload)
    response = jsonify(venue_id)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run(host="192.168.45.156", debug=True, port=5000)
