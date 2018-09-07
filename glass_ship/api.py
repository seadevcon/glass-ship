from flask import request, jsonify, abort
from flask import Flask
from ship import vesseltrackerservice

app = Flask(__name__)
app.debug = True


@app.route("/hello")
def main():
    return jsonify({"Message": "Hello!"})

@app.route('/ship', methods=['GET'])
def get_ship():
    response = vesseltrackerservice.get_ships(ion=50, lat=50, range=1000000000)
    return response.text, response.status_code
