
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

class clsuser():

    """
        @brief Funcion que inserta un nuevo usuario a la base de datos
        
        @param 
                
        @return True si se inserta. De lo contrario False.
    """
        
    def insertar(self, newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole):
        nuevoUsuario=model.User()
        
     
    
    def modify_fullname(self, fullname, newFullname):
        session.query(model.User).filter(model.User.fullname==fullname).\
        update({'fullname':(newFullname)})
        session.commit()    
 
                
    def buscar(self,fullname):
         
        fullnameEsEntero = (type(fullname) == int)
        
        if(fullnameEsEntero):
            busqueda= session.query(model.User).filter(model.User.fullname==fullname).all()
            return(buesqueda)
        
        return None
        
    def modificar(self):
        pass
   
    def eliminar(self, username):
        session.query(model.User).filter(model.User.username==username).delete()
        session.commit()
    
