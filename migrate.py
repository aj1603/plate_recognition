from main import db, app

from main.models import (
    Car
)

from main.db_migration_data.car_config import cars


with app.app_context():
    db.drop_all()
    db.create_all()

    for car in cars:
        db_car = Car(**car)
        db.session.add(db_car)
        db.session.commit()