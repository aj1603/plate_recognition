import os
from posixpath import splitext
from flask import request, make_response, url_for, render_template, jsonify, request
import requests, json, time
from datetime import datetime, timedelta
from main import app, db
from main.config import Config
from main.models import Car
from .forms import CarForm, CarUpdateForm
from distutils.sysconfig import get_makefile_filename
from flask import Blueprint, session, redirect, render_template, flash, make_response, request, url_for
import requests
from sqlalchemy import null

id = 0
delay_seconds = 10
last_time = datetime.now()
door_server_url = "http://192.168.0.105"
timer = time.time()
global plateid
plateid = 0

# @app.route('/update_discount', methods=['GET', 'POST'])
# def update_discount():
#         return render_template("game.html")

@app.route('/', methods=['GET', 'POST'])
def index():
		return "App is working"


@app.route('/car', methods=['GET', 'POST'])
def car():
    global plateid
    if request.method == "POST":
        req = request.get_json()
        plate = req.get("plate")
        plate2 = plate.split(" ")[0]
        plate3 = plate.split(" ")[1]
        plate4 = plate.split(" ")[2]
        plate5 = (plate2 + plate3)
        print(plate5)
        plate7 = Car.query.filter_by(uni_plate = plate5).first()
        if plate7:
            plateid=plate7.id
            try:
                print("sending")
                r = requests.get(
                    "{}{}".format(door_server_url,"/control/1"),
                headers = {'Content-Type': 'application/json'})
            except Exception as ex:
                print(ex)
        return "ok"
    if request.method == 'GET':
        print(plateid)
        plate6 = Car.query.filter_by(id = plateid).first()
        res = plate6.json()
        res1 = {
            "data": res,
        }
        return render_template("car_data.html", res = res1)

@app.route('/all_cars/', methods =["GET", "POST"])
def all_cars():
    if request.method == 'GET':
        cars = Car.query.all()
        return render_template("all_cars.html", cars = cars)

@app.route('/add_car', methods=['GET', 'POST'])
def add_car():
    form = CarForm()
    if form.validate_on_submit():
        new_client = Car.query.filter_by(plate=form.plate.data).first()
        print(new_client)
        if new_client is None:
            splittt = form.plate.data
            splitext = splittt.split(' ')
            splitext0 = splitext[0]
            splitext1 = splitext[1]
            splitext2 = splitext[2]
            new_client = Car(driver_name=form.driver_name.data, driver_surname=form.driver_surname.data, car_name = form.car_name.data, plate=form.plate.data,
                            plate_first = splitext0, plate_num = splitext1, plate_last = splitext2, uni_plate=splitext0+splitext1)
            db.session.add(new_client)
            db.session.commit()
        form.driver_name.data = ''
        form.driver_surname.data = ''
        form.car_name.data = ''
        form.plate.data = ''
    return render_template('add_car.html', form=form)

@app.route('/car/<int:id>/update/', methods=['GET', 'POST'])
def update_car(id):
    car = Car.query.get_or_404(id)
    form = CarUpdateForm()
    if form.validate_on_submit():
        car.driver_name = form.driver_name.data
        car.driver_surname = form.driver_surname.data
        car.car_name = form.car_name.data
        car.plate = form.plate.data
        splittt = form.plate.data
        splitext = splittt.split(' ')
        splitext0 = splitext[0]
        splitext1 = splitext[1]
        splitext2 = splitext[2]
        car.plate_first = splitext0
        car.plate_num = splitext1
        car.plate_last = splitext2
        car.uni_plate=splitext0+splitext1
        db.session.commit()
        cars = Car.query.all()
        return render_template("all_cars.html", cars=cars)
    elif request.method == 'GET':
        form.driver_name.data = car.driver_name
        form.driver_surname.data = car.driver_surname
        form.car_name.data = car.car_name
        form.plate.data = car.plate
        return render_template("edit_car.html", form=form)

@app.route('/car/<int:id>/delete/', methods=['GET', 'POST'])
def delete_car(id):
    delete_car = Car.query.get_or_404(id)
    db.session.delete(delete_car)
    db.session.commit()
    cars = Car.query.all()
    return render_template("all_cars.html", cars=cars)