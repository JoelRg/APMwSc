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
        if not(self.buscar()):  # preguntamos si existe otro departamento con el mismo id
             # insertamos
            odpt= clsdpt(self.iddpt,self.namedpt)
            db.session.add(me)
            db.session.commit()
            return True 
        else:
            return False
                
    def buscar(self):
        odpt= clsdpt.query.filter_by(iddpt=self.iddpt).first()     
        if odpt is None:  
            return False
        
    def modificar(self):
        if (self.buscar()!=None): # vemos si existe
            return self.eliminar() and self.insertar()
        else:
            return False
   
    def eliminar(self):
        if (self.buscar()!=None):  #Consultamos si esta la instancia a eliminar
            # eliminamos
            odpt= clsdpt(self.iddpt)
            db.session.delete(me)
            db.session.commit()
            return True 
        else:
            return False  
    
