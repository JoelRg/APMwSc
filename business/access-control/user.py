
# Librerias a utilizar.

import os
import sys
from sqlalchemy.sql.expression import except_
from checkbox.properties import String

# PATH que permite utilizar al modulo "model.py"

sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Se realiza la conexion con la bases de datos para realizar cambios en ella.
DBSession = sessionmaker(bind=model.engine)
session = DBSession()

class clsUser():
        
    def insertar(self,fullname, nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole):
        
        fullnameEsCadena = type(fullname) == str
        if fullnameEsCadena:
            if self.buscar(fullname) == []:
                try: # Preguntamos si hay problemas con las claves primarias y foraneas
                    nuevoUsuario=model.User(fullname, nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole)
                    session.add(nuevoUsuario)
                    session.commit()           
                    return True
                except: 
                    return False
        
        return False
     
    
    def modificarUserName(self, fullname,nuevoUsername):
        
        if  (self.buscar(fullname) == []):
            return False
       
        try:
            
            session.query(model.User).filter(model.User.fullname==fullname).\
                update({'username':(nuevoUsername)})
            session.commit()
            
            return True 
        except:
            return False      
        
    def modificarPassword(self, fullname,nuevoPassword):
        
        if  (self.buscar(fullname) == []):
            return False
       
        try:
            
            session.query(model.User).filter(model.User.fullname==fullname).\
                update({'password':(nuevoPassword)})
            session.commit()
            
            return True 
        except:
            return False    
        
    def modificarEmail(self, fullname,nuevoEmail):
        
        if  (self.buscar(fullname) == []):
            return False
       
        try:
            
            session.query(model.User).filter(model.User.fullname==fullname).\
                update({'email':(nuevoEmail)})
            session.commit()
            
            return True 
        except:
            return False   
        
    def modificarIddpt(self, fullname,nuevoIddpt):
        
        if  (self.buscar(fullname) == []):
            return False
       
        try:
            session.query(model.User).filter(model.User.fullname==fullname).\
                update({'iddpt':(nuevoIddpt)})
            session.commit()
            
            return True 
        except:
            return False    
        
    def modificarIdrole(self, fullname,nuevoIdrole):
        
        if  (self.buscar(fullname) == []):
            return False
       
        try:
            
            session.query(model.User).filter(model.User.fullname==fullname).\
                update({'idrole':(nuevoIdrole)})
            session.commit()
            
            return True 
        except:
            return False              
         
                
    def buscar(self,fullname):
         
        fullnameEsCadena = (type(fullname) == str)
        
        if fullnameEsCadena:
            try:
                busqueda= session.query(model.User).filter(model.User.fullname==fullname).all()
                return busqueda
            except: 
                return []

        return []
   
    def eliminar(self, fullname):
        
        if not(self.buscar(fullname )==[]):
            try:
                session.query(model.User).filter(model.User.fullname==fullname).delete()
                session.commit()
                return True
            except:
                return False
            
        return False
