from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class EmpleadoForm(FlaskForm):
    nombre =StringField("Nombre",validators=[DataRequired()])
    apellido = StringField("Apellido")
    gradoAcademico = StringField ("Grado academico", validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class EquipoForm(FlaskForm):
    marca =StringField("Marca",validators=[DataRequired()])
    modelo = StringField("Modelo",validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class AutoForm(FlaskForm):
    marca =StringField("Marca",validators=[DataRequired()])
    modelo = StringField("Modelo",validators=[DataRequired()])
    anoDeSalida = StringField ("Año de salida", validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class CelularForm(FlaskForm):
    marca =StringField("Marca",validators=[DataRequired()])
    modelo = StringField("Modelo",validators=[DataRequired()])
    sistemaOperativo = StringField ("Sistema operativo", validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class AlbumForm(FlaskForm):
    nombre =StringField("Nombre",validators=[DataRequired()])
    banda = StringField("Banda",validators=[DataRequired()])
    genero = StringField ("Genero", validators=[DataRequired()])
    enviar = SubmitField('Enviar')