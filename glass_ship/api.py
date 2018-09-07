from flask import Flask
from flask import jsonify
from glass_ship.ship import vesseltrackerservice
from glass_ship.storage.db import init_db, engine
from sqlalchemy.orm import sessionmaker, Query
from glass_ship.storage import models
from glass_ship.helpers import vessel_parsing_helper

app = Flask("glass-ship")
app.debug = True
init_db()
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/get_ships_names')
def get_ship_names():
    vessels = vessel_parsing_helper.get_vessel_name_list(models.Vessel.query.all())
    return jsonify({"name": vessels}), 200

@app.route('/get_ships_names_by_flag')
def get_all_ships_by_flag(flag):
    vessels = vessel_parsing_helper.get_vessel_name_list(session.query(models.Vessel).filter(models.Vessel.flag == flag))
    return jsonify({"name": vessels}), 200

@app.route('/insert_ships', methods=['GET'])
def insert_ships():
    vesseltrackerservice.store_vessels_in_database(session)
    return jsonify({"message": "I inserted all the ships, if you refresh this I will insert them again.. and again.. so don't do this"})
