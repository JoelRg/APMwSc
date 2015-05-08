'''
Created on 8/5/2015

@author: joel
'''

from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy 
 
app = Flask(__name__) 
app.config.from_object('config') 
db = SQLAlchemy(app) 
 
from app import views, models 

class clsuser(db.Model):
    fullname = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(128), unique=True)
    email =db.Column(db.String(30), unique=True)
    iddpt = db.Column(db.Integer, db.ForeignKey('clsdpt.iddpt'))
    idrole = db.Column(db.Integer, db.ForeignKey('clsrole.idrole'))
    
    def __init__(self, fullname, username, password, email, iddpt, idrole):
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.iddpt = iddpt 
         
    def insertar(self):
        pass
    
    def buscar(self):
        pass
    
    def modificar(self):
        pass
    
    def eliminar(self):
        pass        
    
    