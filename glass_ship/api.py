from flask import Flask
from flask import jsonify
from glass_ship.ship import vesseltrackerservice
from glass_ship.storage.db import init_db, engine
from sqlalchemy.orm import sessionmaker

app = Flask("glass-ship")
app.debug = True
init_db()
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/ship', methods=['GET'])
def get_ship():
    response = vesseltrackerservice.get_all_ships(lon=50, lat=50, range=1000000000)
    return jsonify({"response_txt": response.text})

@app.route('/insert_ships', methods=['GET'])
def insert_ships():
    vesseltrackerservice.store_vessels_in_database(session)
    return jsonify({"message": "I inserted all the ships, if you refresh this I will insert them again.. and again.. so don't do this"})
