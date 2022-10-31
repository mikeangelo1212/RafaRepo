from app import db

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    nombre= db.Column(db.String(250))
    apellido=db.Column(db.String(250))
    gradoAcademico=db.Column(db.String(250))

    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Nombre:{self.nombre}
        Apellido:{self.apellido}
        Grado academico:{self.gradoAcademico}"""
        )

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    marca= db.Column(db.String(250))
    modelo=db.Column(db.String(250))
    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Marca y modelo:{self.marca} {self.modelo}"""
        )

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    marca=db.Column(db.String(250))    
    modelo=db.Column(db.String(250))
    anoDeSalida= db.Column(db.Integer)
    
    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Modelo:{self.modelo} 
        Marca: {self.marca} 
        Año: {self.anoDeSalida}"""
        )

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    modelo=db.Column(db.String(250))    
    marca=db.Column(db.String(250))
    sistemaOperativo= db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Modelo:{self.modelo} 
        Marca: {self.marca} 
        Sistema Operativo: {self.sistemaOperativo}"""
        )

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    nombre=db.Column(db.String(250))    
    banda=db.Column(db.String(250))
    genero= db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Nombre:{self.nombre} 
        Banda: {self.banda} 
        Genero: {self.genero}"""
        )