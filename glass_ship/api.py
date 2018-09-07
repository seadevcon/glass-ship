from flask import Flask
from flask import jsonify, request
from glass_ship.ship import vesseltrackerservice
from glass_ship.storage.models import Seafarer
from glass_ship.storage.db import init_db, engine
from sqlalchemy.orm import sessionmaker

app = Flask("glass-ship")
app.debug = True
init_db()
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/ship', methods=['GET'])
def get_ship():
    response = vesseltrackerservice.get_ships(ion=50, lat=50, range=1000000000)
    vesseltrackerservice.store_vessels_in_database(session)
    return jsonify({"response_txt": response.text})


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
                                            Seafarer.sailor_id == data['sailor_id']).first():
        session.add(user)
        session.commit()
    else:
        return jsonify({"Message": "User already exists"}), 200
    return jsonify({"Message": "Saved user!"}), 200


