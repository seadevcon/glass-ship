"""  create tables definition """

from sqlalchemy import Column, Integer, String,
from application.databases import Base

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
    ship_class = Column(Char)
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