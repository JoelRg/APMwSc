
# Librerias a utilizar.

import os
import sys
from sqlalchemy.sql.expression import except_

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
        
    def insertar(self,fullname, nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole):
        
        fullnameEsCadena = (type(fullname) == str)
        if fullnameEsCadena:
            if (self.buscar(fullname) == []):
                try: # si hay problema
                    nuevoUsuario=model.User(fullname, nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole)
                    session.add(nuevoUsuario)
                    session.commit()           
                    return True
                except: 
                    return False
        
        return False
     
    
    def modificar(self, fullname,nuevoUsername,nuevoPassword, nuevoEmail, nuevoIddpt, nuevoIdrole):
        
        if (self.buscar(fullname) == []):
           return False
       
        try:
            session.query(model.User).filter(model.User.fullname==fullname).\
            update({'fullname':(fullname)},{'username':(nuevoUsername)},{'password':(nuevoPassword)},
                   {'email':(nuevoEmail)},{'iddpt':(nuevoIddpt)},{'idrole':(nuevoIdrole)})
            session.commit()
            return True 
        except:
            return False
        
      
                
    def buscar(self,fullname):
         
        fullnameEsCadena = (type(fullname) == str)
        
        if( fullnameEsCadena):
            try:
                busqueda= session.query(model.User).filter(model.User.fullname==fullname).all()
                return busqueda
            except:
                return []

        return []
   
    def eliminar(self, fullname):
        
        if not(self.buscar(fullname )==[]):
            session.query(model.User).filter(model.User.fullname==fullname).delete()
            session.commit()
            return True
        
        return False
