import requests
from flask import jsonify
import ssl
import flask
from models import Vessels

token = "12345678-1234-1234-1234-1234567890ab"
base_vesseltracker_url = "https://api.vesseltracker.com/api/v1/"

def get_all_ships():
    endpoint = "https://ais.spire.com/vessels/"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjdXN0b21lciI6eyJpZCI6IjQ0NCIsIm5hbWUiOiJTZWFkZXZjb24gLSBIYWNrYXRob24gVGVtcG9yYXJ5IiwidXVpZCI6IjQ0NCJ9LCJpc3MiOiJzcGlyZS5jb20iLCJpYXQiOjE1MzU1NDcxMTN9.E72ji2Kt4bfREE_0LoyaWL2aPMwVvbIIKd3xPkx4FtI"
    response = requests.get(endpoint, headers={'Authorization': "Bearer {}".format(token)})

    with open("vessels.txt", 'w') as outfile:
        outfile.write(response.text)


def store_vessels_in_database():
    json_string = ""

    with open("vessels.txt", 'r') as infile:
        for line in infile:
            json_string = json_string + line

    file = open("vessels.txt", 'r')
    json = flask.json.load(file)

    for vessel in json["data"]:
        vessel = new


store_vessels_in_database()

