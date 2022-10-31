from app import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    nombre= db.Column(db.String(250))
    apellido=db.Column(db.String(250))
    email=db.Column(db.String(250))
    direcciones = db.relationship('Direccion', backref='persona')

    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Nombre:{self.nombre}
        Apellido:{self.apellido}
        Email:{self.email}"""
        )

class Direccion(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    numero= db.Column(db.Integer)
    calle=db.Column(db.String(250))
    idpersona=db.Column(db.Integer,db.ForeignKey('persona.id'),nullable=False)
    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Calle con numero:{self.calle} {self.numero}"""
        )

class Perro(db.Model):
    id = db.Column(db.Integer, primary_key=True)#a diferencia de django, aqui si debemos declarar nuestra llave
    nombre=db.Column(db.String(250))    
    raza=db.Column(db.String(250))
    edad= db.Column(db.Integer)
    
    def __str__(self) -> str:
        return (
        f"""ID:{self.id} 
        Nombre:{self.nombre} 
        Raza: {self.raza} 
        Edad: {self.edad}"""
        )