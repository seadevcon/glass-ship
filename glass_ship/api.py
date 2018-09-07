from flask import Flask
from flask import jsonify
from glass_ship.ship import vesseltrackerservice
from glass_ship.storage.db import init_db, engine
from sqlalchemy.orm import sessionmaker
from glass_ship.storage import models


app = Flask("glass-ship")
app.debug = True
init_db()
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/get_ships_names')
def get_ship_names():
    vessels = models.Vessel.query.all()
    vessel_list = []
    for vessel in vessels:
        vessel_list.add(vessel.name)

    return jsonify({"name": vessel_list}), 200

