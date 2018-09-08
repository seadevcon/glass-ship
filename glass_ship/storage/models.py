"""  create tables definition """
from sqlalchemy import Column, Integer, String, CHAR, DateTime
from glass_ship.storage.db import Base


class Vessel(Base):
    """
    Vessel object

    data from spire regarding vessels
    "id": "b2c2626d-ff0b-4892-8262-5acae60946a4",
    "name": "JUPITER II",
    "mmsi": 701000533,
    "imo": 9123726,
    "ship_type": "Fishing",
    "class": "A",
    "flag": "AR",
    "length": 27,
    "width": 7,
    "person_capacity": 8,
    """
    __tablename__ = 'vessel'

    id = Column(Integer, primary_key=True, unique=True)
    ship_id = Column(String(120), unique=True)
    name = Column(String(120))
    mmsi = Column(String(120))
    imo = Column(Integer)
    ship_type = Column(String(120))
    ship_class = Column(CHAR)
    flag = (String(10))
    length = (Integer)
    width = (Integer)
    person_capacity = (Integer)

    def __init__(self, ship_id, name, mmsi, imo, ship_type, ship_class, flag, length, width, person_capacity):
        self.ship_id = ship_id
        self.name = name
        self.mmsi = mmsi
        self.imo = imo
        self.ship_type = ship_type
        self.ship_class = ship_class
        self.flag = flag
        self.length = length
        self.width = width
        self.person_capacity = person_capacity


class Seafarer(Base):
    """ 
    User Login object
    """
    __tablename__ = 'seafarer'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(120))
    sailor_id = Column(String(120))
    phone = Column(String(20))
    emergency_contact = Column(String(50))

    def __init__(self, name, sailor_id, phone, emergency_contact):
        self.name = name
        self.sailor_id = sailor_id
        self.phone = phone
        self.emergency_contact = emergency_contact


class Distress(Base):
    """
    User Distress object
    """
    __tablename__= 'distress'

    id = Column(Integer, primary_key=True, unique=True)
    timestamp = Column(DateTime)
    user_name = Column(String(120))
    ship_name = Column(String(120))
    distress_type = Column(String(30))

    def __init__(self, timestamp, user_name, ship_name, distress_type):
        self.timestamp = timestamp
        self.user_name = user_name
        self.ship_name = ship_name
        self.distress_type = distress_type


class Report(Base):
    """
    User Report object
    """
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True, unique=True)
    timestamp = Column(DateTime)
    device_id = Column(String(120))
    user_name = Column(String(120))
    ship_name = Column(String(120))
    food = Column(Integer)
    water = Column(Integer)
    bedding = Column(Integer)
    health = Column(Integer)
    wage = Column(Integer)
    happiness = Column(Integer)
    overallrating = Column(Integer)

    def __init__(self, timestamp, device_id, user_name, ship_name, food, water, bedding, health, wage, happiness, overallrating):
        self.timestamp = timestamp
        self.device_id = device_id
        self.user_name = user_name
        self.ship_name = ship_name
        self.food = food
        self.water = water
        self.bedding = bedding
        self.health = health
        self.wage = wage
        self.happiness = happiness
        self.overallrating = overallrating
