from flask import Flask
from flask import jsonify, request
from glass_ship.ship import vesseltrackerservice
from glass_ship.storage.models import Seafarer, Distress
from glass_ship.storage.db import init_db, engine
from sqlalchemy.orm import sessionmaker
from glass_ship.storage import models
import datetime

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
        vessel_list.append(vessel.name)

    return jsonify({"name": vessel_list}), 200


@app.route('/register', methods=['POST'])
def store_user():
    """
    Store user into db
    :return: json response
    """
    data = request.get_json()
    user = Seafarer(name=data['name'], sailor_id=data['sailorID'],
                    phone=data['phone'], emergency_contact=data['emergencyContact'])
    if not session.query(Seafarer).filter(Seafarer.name == data['name'],
                                            Seafarer.sailor_id == data['sailorID']).first():
        session.add(user)
        session.commit()
    else:
        return jsonify({"Message": "User already exists"}), 200
    return jsonify({"Message": "Saved user!"}), 200


@app.route('/add_distress', methods=['POST'])
def store_distress():
    """
    Store user distress call into db, it can be of three types: injury, abandon, missing person
    :return: json response
    """
    data = request.get_json()
    distress = Distress(timestamp=datetime.datetime.today(), user_name=data['name'], ship_name=data['ship_name'],
                        distress_type=data['distress_type'])
    if not session.query(Seafarer).filter(Seafarer.name == data['name']).first():
        return jsonify({"Message":"User is not logged in"}), 400
    
    session.add(distress)
    session.commit()    
    return jsonify({"Message":"Saved distress call"})


@app.route('/insert_ships', methods=['GET'])
def insert_ships():
    vesseltrackerservice.store_vessels_in_database(session)
    return jsonify({"message": "I inserted all the ships, if you refresh this I will insert them again.. and again.. so don't do this"})
