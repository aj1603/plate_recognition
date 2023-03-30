from lib2to3.pgen2 import driver
from main import app, db
from sqlalchemy.dialects.postgresql import JSON


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    driver_name = db.Column(db.String(100))
    driver_surname = db.Column(db.String(100))
    car_name = db.Column(db.String(50))
    plate = db.Column(db.String(50), unique=True)
    plate_first = db.Column(db.String(50))
    plate_num = db.Column(db.String(50))
    plate_last = db.Column(db.String(50))
    uni_plate = db.Column(db.String(50), unique=True)

    def json(self):
        car = {
            "id": self.id,
            "driver_name": self.driver_name,
            "driver_surname": self.driver_surname,
            "car_name": self.car_name,
            "plate": self.plate,
            "plate_first": self.plate_first,
            "plate_num": self.plate_num,
            "plate_last": self.plate_last,
            "uni_plate": self.uni_plate,
        }
        return car

    def __repr__(self):
        return f"Car('{self.id}', '{self.driver_name}', '{self.driver_surname}','{self.car_name}', '{self.plate}', '{self.plate_first}', '{self.plate_num}', '{self.plate_last}', '{self.uni_plate}')"