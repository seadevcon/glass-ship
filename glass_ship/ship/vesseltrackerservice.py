from flask import request
from flask import jsonify
import ssl
import flask
from glass_ship.storage.models import Vessel

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6eyJpZCI6IjQ0NCIsIm5hbWUiOiJTZWFkZXZjb24gLSBIYWNrYXRob24gVGVtcG9yYXJ5IiwidXVpZCI6IjQ0NCJ9LCJpc3MiOiJzcGlyZS5jb20iLCJpYXQiOjE1MzU1NDcxMTN9.E72ji2Kt4bfREE_0LoyaWL2aPMwVvbIIKd3xPkx4FtI"
endpoint = "https://ais.spire.com/vessels/"

def get_all_ships():
    response = request.get(endpoint, headers={'Authorization': "Bearer {}".format(token)})

    with open("vessels.txt", 'w') as outfile:
        outfile.write(response.text)

def store_vessels_in_database(session):
    file = open("glass_ship/ship/vessels.txt", 'r')
    json = flask.json.load(file)

#   def __init__(self, ship_id, name, mmsi, imo, ship_type, ship_class, flag, length, width, person_capacity):
    for vessel in json["data"]:
        vessel = Vessel(vessel["id"], vessel["name"], vessel["mmsi"], vessel["imo"], vessel["ship_type"],
                               vessel["class"], vessel["flag"], vessel["length"],
                               vessel["width"], vessel["person_capacity"])
        session.add(vessel)
    
    session.commit()

