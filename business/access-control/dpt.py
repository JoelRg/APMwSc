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

class clsDpt(db.model):
    
    iddpt = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)

    def __init__(self,iddpt,namedpt):
        self.iddpt = iddpt 
        self.namedpt= namedpt
     
    def insertar(self):
        pass
    
    def buscar(self):
        pass
    
    def modificar(self):
        pass
    
    def eliminar(self):
        pass    
    
