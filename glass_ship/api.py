from flask import request, jsonify, abort

from flask import Flask

app = Flask("glass-ship")
app.debug = True
from glass_ship.storage.db import init_db
init_db()


@app.route("/test")
def main():
    return jsonify({"Message": "Hello!"})
