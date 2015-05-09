

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


class clsDpt():
    
    def insertar(self,iddpt,namedpt):
        
        if self.buscar(iddpt) == None:
            nuevoDepartamento=model.Dpt(iddpt,namedpt)
            session.add(nuevoDepartamento)
            session.commit()           
            return True
        
        return False
                
    def buscar(self,iddpt):
         
        iddptEsEntero = (type(iddpt) == int)
        
        if(iddptEsEntero):
            busqueda= session.query(model.Dpt).filter(model.Dpt.iddpt==iddpt).first()
            return(buesqueda)
        
        return None
        
    def modificar(self,iddpt,namedpt):
        
        if (self.buscar(iddpt)!=None): # vemos si existe
            return self.eliminar(iddpt) and self.insertar(iddpt,namedpt) #eliminamos e insertamos
       
        return False
   
    def eliminar(self,iddpt):
        if (self.buscar(iddpt)!=None):  #Consultamos si esta la instancia a eliminar
            # eliminamos
            session.query(model.Dpt).filter(model.Dpt.iddpt==iddpt).delete()
            session.commit()
            return True
         
        return False

