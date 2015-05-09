
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

class clsUser():

    """
        @brief Funcion que inserta un nuevo usuario a la base de datos
        
        @param 
                
        @return True si se inserta. De lo contrario False.
    """
        
    def insertar(self, nuevoFullname, nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole):
        if self.buscar(nuevofullname) == None:
            nuevoUsuario=model.User(nuevoFullname, nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole)
            session.add(nuevoUsuario)
            session.commit()           
            return True
        
        return False
     
    
    def modificar(self, fullname,nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole):
        
        if self.buscar(fullname) != None:
            return self.eliminar(fullname) and self.insertar(Fullname, nuevoUsername, nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole)
        
        return False
                
    def buscar(self,fullname):
         
        fullnameEsEntero = (type(fullname) == int)
        
        if(fullnameEsEntero):
            busqueda= session.query(model.User).filter(model.User.fullname==fullname).first()
            return(buesqueda)
        
        return None

   
    def eliminar(self, fullname):
        if self.buscar(fullname )!=None:
            session.query(model.User).filter(model.User.fullname==fullname).delete()
            session.commit()
            return True
        
        return False
