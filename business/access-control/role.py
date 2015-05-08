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

class clsrole(db.Model):
    
    idrole= db.Column(db.Integer, primary_key=True)
    namerole= db.Column(db.String(50), unique=True)
    
    def __init__(self, idrole, namerole):
        self.idrole = idrole    
        self.namerole = namerole
        
    def insertar(self):
        pass
    
    def buscar(self):
        pass
    
    def modificar(self):
        pass
    
    def eliminar(self):
        pass    
    