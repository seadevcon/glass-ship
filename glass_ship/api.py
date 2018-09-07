from flask import request, jsonify, abort

from flask import Flask

app = Flask("glass-ship")
app.debug = True


@app.route("/test")
def main():
    return jsonify({"Message": "Hello!"})
