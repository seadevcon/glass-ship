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
    response = vesseltrackerservice.get_ships(ion=50, lat=50, range=1000000000)
    vesseltrackerservice.store_vessels_in_database(session)
    return jsonify({"response_txt": response.text})

