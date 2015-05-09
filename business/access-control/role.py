
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
    
    def insertar(self,idrole,namerole):
        if self.buscar(idrole) == None:
            nuevoRole=model.Role(idrole,namerole)
            session.add(nuevoRole)
            session.commit()           
            return True
        
        return False
                
    def buscar(self,idrole):
         
        idroleEsEntero = (type(idrole) == int)
        
        if(idroleEsEntero):
            busqueda= session.query(model.Role).filter(model.Role.idrole==idrole).first()
            return(buesqueda)
        
        return None
        
    def modificar(self,idrole,namerole):
        
        if (self.buscar(idrole)!=None): # vemos si existe
            return self.eliminar(idrole) and self.insertar(idrole,namerole) #eliminamos e insertamos
       
        return False
   
    def eliminar(self,idrole):
        if (self.buscar(idrole)!=None):  #Consultamos si esta la instancia a eliminar
            # eliminamos
            session.query(model.Role).filter(model.Role.idrole==idrole).delete()
            session.commit()
            return True
         
        return False


    
    