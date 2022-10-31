from flask import Flask
from database import db

app=Flask(__name__)

#configuracion de la db
USER_DB='postgres'
PASS_DB= 'admin'
URL_DB = 'localhsot'
NAME_DB= 'flaskdb'
FULL_URL_DB=f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATBASE_URI'] =FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)