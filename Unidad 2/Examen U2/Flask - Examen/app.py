from flask import Flask, request,url_for,render_template,redirect,jsonify,session
from database import db
from flask_migrate import Migrate
from models import Empleado,Equipo,Auto,Album,Celular
from forms import EmpleadoForm,EquipoForm,AutoForm,AlbumForm,CelularForm
from werkzeug.exceptions import abort
#import logging
#CRUD solo disponible en las primeras dos entidades

app = Flask(__name__)

#Config Database
USER_DB = "postgres"
PASS_DB = "admin"
URL_DB = "localhost"
NAME_DB = "flaskExa"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#Config Migrate

migrar = Migrate()
migrar.init_app(app,db)

app.config['SECRET_KEY']='1212'

#logging.basicConfig(filename='error.log',level=logging.DEBUG)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
        #app.logger.debug(request.headers.get('token'))
        #app.logger.debug(request.headers.get('token'))
        #Empleado,Equipo,Auto,Album,Celular
        empleados =  Empleado.query.all()
        equipos =Equipo.query.all()
        autos = Auto.query.all()
        albumes=Album.query.all()
        celulares=Celular.query.all()
        return render_template("index.html",
        empleados = empleados,
        equipos=equipos,
        autos=autos,
        albumes=albumes,
        celulares=celulares)

    

#=====================================DETALLES======================================
#Empleado,Equipo,Auto,Album,Celular
@app.route('/verEmpleado/<int:id>')
def verDetalleEmpleado(id):
    empleado = Empleado.query.get_or_404(id)
    return render_template('detalleEmpleado.html',empleado = empleado)

@app.route('/verEquipo/<int:id>')
def verDetalleEquipo(id):
    equipo = Equipo.query.get_or_404(id)
    return render_template('detalleEquipo.html',equipo = equipo)

@app.route('/verAuto/<int:id>')
def verDetalleAuto(id):
    auto = Auto.query.get_or_404(id)
    return render_template('detalleAuto.html',auto=auto)

@app.route('/verAlbum/<int:id>')
def verDetalleAlbum(id):
    album = Album.query.get_or_404(id)
    return render_template('detalleAlbum.html',album = album)

@app.route('/verCelular/<int:id>')
def verDetalleCelular(id):
    celular = Celular.query.get_or_404(id)
    return render_template('detalleCelular.html',celular = celular)

#======================================AGREGAR======================================
#Empleado,Equipo,Auto,Album,Celular
@app.route('/agregarEmpleado',methods=['GET','POST'])
def agregarEmpleado():
    #app.logger.debug(request.headers.get('token'))
    empleado = Empleado()
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == "POST":
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            #Insert
            db.session.add(empleado)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarEmpleado.html',forma = empleadoForm)

@app.route('/agregarEquipo',methods=['GET','POST'])
def agregarEquipo():
    #app.logger.debug(request.headers.get('token'))
    equipo = Equipo()
    equipoForm = EquipoForm(obj=equipo)
    #agregando un combobox con una query
    if request.method == "POST":
        if equipoForm.validate_on_submit():
            equipoForm.populate_obj(equipo)
            #Insert
            db.session.add(equipo)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarEquipo.html',forma = equipoForm)

@app.route('/agregarAuto',methods=['GET','POST'])
def agregarAuto():
    #app.logger.debug(request.headers.get('token'))
    auto = Auto()
    autoForm = AutoForm(obj=auto)
    if request.method == "POST":
        if autoForm.validate_on_submit():
            autoForm.populate_obj(auto)
            #Insert
            db.session.add(auto)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarAuto.html',forma = autoForm)

@app.route('/agregarAlbum',methods=['GET','POST'])
def agregarAlbum():
    album = Album()
    albumForm = AlbumForm(obj=album)
    if request.method == "POST":
        if albumForm.validate_on_submit():
            albumForm.populate_obj(album)
            #Insert
            db.session.add(album)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarAlbum.html',forma = albumForm)

@app.route('/agregarCelular',methods=['GET','POST'])
def agregarCelular():
    celular = Celular()
    celularForm = CelularForm(obj=celular)
    if request.method == "POST":
        if celularForm.validate_on_submit():
            celularForm.populate_obj(celular)
            #Insert
            db.session.add(celular)
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('agregarCelular.html',forma = celularForm)


#==================================EDITAR======================================
#Empleado,Equipo,Auto,Album,Celular
@app.route('/editarEmpleado/<int:id>',methods=['GET','POST'])
def editarEmpleado(id):
    empleado = Empleado.query.get_or_404(id)
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method == "POST":
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarEmpleado.html',forma = empleadoForm)

@app.route('/editarEquipo/<int:id>',methods=['GET','POST'])
def editarEquipo(id):
    #app.logger.debug(request.headers.get('token'))
    equipo = Equipo.query.get_or_404(id)
    equipoForm = EquipoForm(obj=equipo)
    if request.method == "POST":
        if equipoForm.validate_on_submit():
            equipoForm.populate_obj(equipo)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarEquipo.html',forma = equipoForm)

@app.route('/editarAuto/<int:id>',methods=['GET','POST'])
def editarAuto(id):
    #app.logger.debug(request.headers.get('token'))
    auto = Auto.query.get_or_404(id)
    autoForm = AutoForm(obj=auto)
    if request.method == "POST":
        if autoForm.validate_on_submit():
            autoForm.populate_obj(auto)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarAuto.html',forma = autoForm)

@app.route('/editarAlbum/<int:id>',methods=['GET','POST'])
def editarAlbum(id):
    album = Album.query.get_or_404(id)
    albumForm = AlbumForm(obj=album)
    if request.method == "POST":
        if albumForm.validate_on_submit():
            albumForm.populate_obj(album)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarAlbum.html',forma = albumForm)

@app.route('/editarCelular/<int:id>',methods=['GET','POST'])
def editarCelular(id):
    celular = Celular.query.get_or_404(id)
    celularForm = CelularForm(obj=celular)
    if request.method == "POST":
        if celularForm.validate_on_submit():
            celularForm.populate_obj(celular)
            #Insert
            db.session.commit()
            return redirect(url_for('inicio'))
    return render_template('editarCelular.html',forma = celularForm)

#=================================ELIMINAR========================================
#Empleado,Equipo,Auto,Album,Celular
@app.route('/eliminarEmpleado/<int:id>')
def eliminarEmpleado(id):
    #app.logger.debug(request.headers.get('token'))
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarEquipo/<int:id>')
def eliminarEquipo(id):
    #app.logger.debug(request.headers.get('token'))
    equipo = Equipo.query.get_or_404(id)
    db.session.delete(equipo)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarAuto/<int:id>')
def eliminarAuto(id):
    #app.logger.debug(request.headers.get('token'))
    auto = Auto.query.get_or_404(id)
    db.session.delete(auto)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarAlbum/<int:id>')
def eliminarAlbum(id):
    album = Album.query.get_or_404(id)
    db.session.delete(album)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/eliminarCelular/<int:id>')
def eliminarCelular(id):
    celular = Celular.query.get_or_404(id)
    db.session.delete(celular)
    db.session.commit()
    return redirect(url_for('inicio'))

#=================Login===================
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        usuario=request.form['username']
        session['username']=usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('inicio'))

#===================Abortar===============
@app.route('/salir')
def salir():
    return abort(404)


@app.errorhandler(404)
def paginaNoEncontrada(error):
    return render_template('404.html',error=error),404

#===========json=============== No funcionaron
@app.route("/eliminarEmpleadoThunder/<int:id>",methods=['DELETE'])#por defecto el method es un get el metodo
def eliminarThunder(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    return "valor eliminado correctamente"