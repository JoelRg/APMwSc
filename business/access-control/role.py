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
        if not(self.buscar()):  # preguntamos si existe otro role con el mismo id
             # insertamos
            orole= clsrole(self.idrole,self.namerole)
            db.session.add(me)
            db.session.commit()
            return True 
        else:
            return False
                
    def buscar(self):
        orole= clsrole.query.filter_by(iddpt=self.idrole).first()     
        if orole is None:  
            return False
        
    def modificar(self):
        if (self.buscar()!=None): # vemos si existe
            return self.eliminar() and self.insertar()
        else:
            return False
   
    def eliminar(self):
        if (self.buscar()!=None):  #Consultamos si esta la instancia a eliminar
            # eliminamos
            orole= clsrole(self.idrole)
            db.session.delete(me)
            db.session.commit()
            return True 
        else:
            return False  
        
        
        
        import os
import sys

# Ruta que permite utilizar el módulo model.py
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declaración de constantes
CONST_MINLEN = 1
CONST_MAXLEN = 50

# Conexión con la base de datos. 
dbsession = sessionmaker(bind= model.engine)
session   = dbsession()
 

class clsRole(object):

    def findNameRole(self, name):
        """Permite buscar un elemento en la base de datos"""
        if type(name) == str:
            if len(name) >= CONST_MINLEN and len(name) <= CONST_MAXLEN:
                found = session.query(model.Role).filter(model.Role.namerole==name).all()
                return found
        return([])
        
    def findIdRole(self, id):
        """Permite buscar un identificador en la base de datos"""
        if type(id) == int:
            found = session.query(model.Role).filter(model.Role.idrole==id).all()
            return found
        return([])
        
    def insertRole(self, namerole):
        """Permite insertar un nuevo rol en la base de datos"""
        if type(namerole) == str:
            if len(namerole) >= CONST_MINLEN and len(namerole) <= CONST_MAXLEN:  
                findName = self.findNameRole(namerole)
        
                if findName == []:
                    newrole = model.Role(namerole)
                    session.add(newrole)
                    session.commit()
                    inserted = self.findIdRole(newrole.idrole)
                    return (inserted != [])
        return False

    def modifyNameRole(self, name, newNameRole):
        validname    = (type(name) == str)
        validnewname = (type(newNameRole) == str)  
        if ((validname) and (validnewname)):
            lengthname    = CONST_MINLEN <= len(name) <= CONST_MAXLEN
            lengthnewname = CONST_MINLEN <= len(newNameRole) <= CONST_MAXLEN
            if ((lengthname) and (lengthnewname)):
                found1 = self.findNameRole(name)
                found2 = self.findNameRole(newNameRole)
                if (found1 != []) and (found2 == []):
                    session.query(model.Role).filter(model.Role.namerole == name).update({'namerole':(newNameRole)})
                    session.commit()
                    return True
        return False    
    