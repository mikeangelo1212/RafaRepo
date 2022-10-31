from flask import Flask, request,url_for,render_template,redirect
from database import db
from flask_migrate import Migrate
from models import Direccion, Persona,Perro
from forms import PersonaForm,DireccionForm,PerroForm
import logging

app = Flask(__name__)

#Config Database
USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "flask_practica"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Config Migrate

migrar = Migrate()
migrar.init_app(app,db)

app.config['SECRET_KEY']='1212'

logging.basicConfig(filename='error.log',level=logging.DEBUG)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    app.logger.debug(request.headers.get('token'))
    app.logger.debug(request.headers.get('token'))
    personas =  Persona.query.all()
    direcciones =Direccion.query.all()
    perros = Perro.query.all()
    return render_template("index.html",personas = personas,direcciones=direcciones,perros=perros)

#=====================================DETALLES======================================
@app.route('/verPersona/<int:id>')
def verDetallePersona(id):
    persona = Persona.query.get_or_404(id)
    return render_template('detallePersona.html',persona = persona)

@app.route('/verDireccion/<int:id>')
def verDetalleDireccion(id):
    direccion = Direccion.query.get_or_404(id)
    return render_template('detalleDireccion.html',direccion = direccion)

@app.route('/verPerro/<int:id>')
def verDetallePerro(id):
    perro = Perro.query.get_or_404(id)
    return render_template('detallePerro.html',perro = perro)

#======================================AGREGAR======================================
@app.route('/agregarPersona',methods=['GET','POST'])
def agregarPersona():
    app.logger.debug(request.headers.get('token'))
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            #Insert
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarPersona.html',forma = personaForm)

@app.route('/agregarDireccion',methods=['GET','POST'])
def agregarDireccion():
    app.logger.debug(request.headers.get('token'))
    direccion = Direccion()
    direccionForm = DireccionForm(obj=direccion)
    personas =  Persona.query.all()
    #("SELECT * FROM Persona order by id")
    #agregando un combobox con una query
    if request.method == "POST":
        if direccionForm.validate_on_submit():
            direccionForm.populate_obj(direccion)
            #Insert
            db.session.add(direccion)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarDireccion.html',personas = personas,forma = direccionForm)

@app.route('/agregarPerro',methods=['GET','POST'])
def agregarPerro():
    app.logger.debug(request.headers.get('token'))
    perro = Perro()
    perroForm = PerroForm(obj=perro)
    if request.method == "POST":
        if perroForm.validate_on_submit():
            perroForm.populate_obj(perro)
            #Insert
            db.session.add(perro)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarPerro.html',forma = perroForm)


#==================================EDITAR======================================
@app.route('/editarPersona/<int:id>',methods=['GET','POST'])
def editarPersona(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == "POST":
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarPersona.html',forma = personaForm)

@app.route('/editarDireccion/<int:id>',methods=['GET','POST'])
def editarDireccion(id):
    app.logger.debug(request.headers.get('token'))
    direccion = Direccion.query.get_or_404(id)
    direccionForm = DireccionForm(obj=direccion)
    if request.method == "POST":
        if direccionForm.validate_on_submit():
            direccionForm.populate_obj(direccion)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarDireccion.html',forma = direccionForm)

@app.route('/editarPerro/<int:id>',methods=['GET','POST'])
def editarPerro(id):
    app.logger.debug(request.headers.get('token'))
    perro = Perro.query.get_or_404(id)
    perroForm = PerroForm(obj=perro)
    if request.method == "POST":
        if perroForm.validate_on_submit():
            perroForm.populate_obj(perro)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarPerro.html',forma = perroForm)

#=================================ELIMINAR========================================
@app.route('/eliminarPersona/<int:id>')
def eliminarPersona(id):
    app.logger.debug(request.headers.get('token'))
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarDireccion/<int:id>')
def eliminarDireccuib(id):
    app.logger.debug(request.headers.get('token'))
    direccion = Direccion.query.get_or_404(id)
    db.session.delete(direccion)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarPerro/<int:id>')
def eliminarPerro(id):
    app.logger.debug(request.headers.get('token'))
    perro = Perro.query.get_or_404(id)
    db.session.delete(perro)
    db.session.commit()
    return redirect(url_for('inicio'))