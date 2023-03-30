from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email

class CarForm(FlaskForm):
    driver_name = StringField('Sürüjiniň ady', validators=[DataRequired()])
    driver_surname = StringField('Sürüjiniň familiýasy', validators=[DataRequired()])
    car_name = StringField('Ulag kysymy', validators=[DataRequired()])
    plate = StringField('Ulagyň belgisi', validators=[DataRequired()])
    submit = SubmitField('Ulag goş')

class CarUpdateForm(FlaskForm):
    driver_name = StringField('Sürüjiniň ady', validators=[DataRequired()])
    driver_surname = StringField('Sürüjiniň familiýasy', validators=[DataRequired()])
    car_name = StringField('Ulag kysymy', validators=[DataRequired()])
    plate = StringField('Ulagyň belgisi', validators=[DataRequired()])
    submit = SubmitField('Ulag goş')