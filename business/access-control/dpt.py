

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
    
    def insertar(self,idDpt,nameDpt):
        
        idDptEsEntero = (type(idDpt) == int)
        if idDptEsEntero and idDpt >=0:
            if self.buscar(idDpt) == []:
                try: # Preguntamos si hay problemas
                    nuevoDpt=model.Dpt(idDpt,nameDpt)
                    session.add(nuevoDpt)
                    session.commit()           
                    return True
                except: 
                    return False
        
        return False
     
    
    def modificar(self,idDpt,nameDpt):
        
        if (self.buscar(idDpt) == []):
           return False
       
        try:
            session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).\
            update({'namedpt':(nameDpt)})
            session.commit()
            return True 
        except:
            return False
        
      
                
    def buscar(self,idDpt):
         
        idDptEsEntero = (type(idDpt) == int)
        
        if idDptEsEntero:
            try:
                busqueda= session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).all()
                return busqueda
            except: 
                return []

        return []
   
    def eliminar(self, idDpt):
        
        if not(self.buscar(idDpt )==[]):
            session.query(model.Dpt).filter(model.Dpt.iddpt==idDpt).delete()
            session.commit()
            return True
        
        return False
    