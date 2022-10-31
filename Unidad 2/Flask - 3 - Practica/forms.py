from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PersonaForm(FlaskForm):
    nombre =StringField("Nombre",validators=[DataRequired()])
    apellido = StringField("Apellido")
    email = StringField ("Email", validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class DireccionForm(FlaskForm):
    numero =StringField("Numero de calle",validators=[DataRequired()])
    calle = StringField("Calle")
    idpersona = StringField ("Id de la Persona", validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class PerroForm(FlaskForm):
    nombre =StringField("Nombre",validators=[DataRequired()])
    raza = StringField("Raza")
    edad = StringField ("Edad", validators=[DataRequired()])
    enviar = SubmitField('Enviar')