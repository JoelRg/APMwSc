
# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Se realiza la conexion con la bases de datos para realizar cambios en ella.
DBSession = sessionmaker(bind=model.engine)
session = DBSession()

class clsRole():
    
    def insertar(self,idRole,nameRole):

        idRoleEsEntero = (type(idRole) == int)
        if idRoleEsEntero and idRole >=0:
            if self.buscar(idRole) == []:
                try: # Preguntamos si hay problemas
                    nuevoRole=model.Role(idRole,nameRole)
                    session.add(nuevoRole)
                    session.commit()           
                    return True
                except: 
                    return False
            
        return False
     
    
    def modificar(self, idRole,nameRole):
        
        if (self.buscar(idRole) == []):
           return False
       
        try:
            session.query(model.Role).filter(model.Role.idrole==idRole).\
            update({'namerole':(nameRole)})
            session.commit()
            return True 
        except:
            return False
        
      
                
    def buscar(self,idRole):
         
        idRoleEsEntero = (type(idRole) == int)
        
        if idRoleEsEntero:
            try:
                busqueda= session.query(model.Role).filter(model.Role.idrole==idRole).all()
                return busqueda
            except: 
                return []

        return []
   
    def eliminar(self, idRole):
        
        if not(self.buscar(idRole )==[]):
            session.query(model.Role).filter(model.Role.idrole==idRole).delete()
            session.commit()
            return True
        
        return False
    
    