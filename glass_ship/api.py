
from flask import request, jsonify, abort
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route("/hello")
def main():
    return jsonify({"Message": "Hello!"})
