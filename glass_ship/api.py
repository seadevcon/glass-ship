from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
from glass_ship.ship import vesseltrackerservice
from glass_ship.storage.models import Seafarer, Distress, Report
from glass_ship.storage.db import init_db, engine
from sqlalchemy.orm import sessionmaker, Query
from glass_ship.storage import models
from glass_ship.helpers import vessel_parsing_helper
import datetime

app = Flask("glass-ship")
CORS(app)
app.debug = True
init_db()
Session = sessionmaker(bind=engine)
session = Session()


@cross_origin()
@app.route('/get_ships_names')
def get_ship_names():
    vessels = vessel_parsing_helper.get_vessel_name_list(models.Vessel.query.all())
    return jsonify({"name": vessels}), 200


@cross_origin()
@app.route('/get_ships_names_by_flag')
def get_all_ships_by_flag(flag):
    vessels = vessel_parsing_helper.get_vessel_name_list(session.query(models.Vessel).filter(models.Vessel.flag == flag))
    return jsonify({"name": vessels}), 200


@cross_origin()
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
        return jsonify({"Message": "User already exists"}), 400
    return jsonify({"Message": "Saved user!"}), 200


@cross_origin()
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
    return jsonify({"Message": "Saved distress call"})


@cross_origin()
@app.route('/rate', methods=['POST'])
def save_rating():
    """
    Save rating for a user
    :return:  response
    """
    data = request.get_json()
    rating = Report(timestamp=datetime.datetime.today(),
                    device_id=data['device_id'],
                    user_name=data['name'],
                    ship_name=data['ship_name'],
                    food=int(data['food']),
                    water=int(data['water']),
                    bedding=int(data['bedding']),
                    health=int(data['health']),
                    wage=int(data['wage']))
    session.add(rating)
    session.commit()
    return jsonify({"Message": "Added new rating"})


@cross_origin()
@app.route('/insert_ships', methods=['GET'])
def insert_ships():
    vesseltrackerservice.store_vessels_in_database(session)
    return jsonify({"message": "I inserted all the ships, if you refresh this I will insert them again.. and again.. so don't do this"})
