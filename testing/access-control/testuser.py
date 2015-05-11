'''
Created on 8/5/2015

@author: joel
'''

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "login.py"
sys.path.append('../../business/access-control')
from user import clsUser, session

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

import unittest



class TestUser(unittest.TestCase):
    
    # FUNCIONES AUXILIATES

        
    def limpiarBaseDeDatos(self):
        # Se limpia la base de datos.      
        session.query(model.User).delete()
        session.query(model.Dpt).delete() 
        session.query(model.Role).delete() 
      
                
              
        # VERIFICACION DE LA CLASE.
    # Test 1: Se crea el objeto clsUser
    
    def test1ObjectExist(self):
        auxUser = clsUser()
        self.assertIsNotNone(auxUser)
        session.query(model.User).delete()  # Se limpia la base de datos.
        
        
        # FUNCION INSERTAR
    ###CASOS FRONTERAS O DE DOMINIO    
    # test 2: Se inserta el usuario cuando la base de datos de Usuario esta vacia.    
    def test2insertar(self):
        self.limpiarBaseDeDatos()        # Se limpia la base de datos
        auxUser = clsUser()       
        
        IdRole = 21
        NameRole = 'rolprobando2'
        RolePrueba = model.Role(IdRole, NameRole)     
        session.add(RolePrueba)
        session.commit()  
         
        IdDpt = 21
        NameDpt = 'dptprobando2'
        DptPrueba = model.Dpt(IdDpt, NameDpt)         
        session.add(DptPrueba)
        session.commit() 
           
        self.assertTrue(auxUser.insertar("Joel Rivas","Hiruma","joelrivas","rivasjoel@gmail.com",21,21),"Correcto")
        self.limpiarBaseDeDatos() 
        
    # test 3: Se inserta el usuario con un id ya perteneciente a la base de datos     
    def test3insertar(self):
        auxUser = clsUser()       
        
        IdRole = 21
        NameRole = 'rolprobando2'
        RolePrueba = model.Role(IdRole, NameRole)     
        session.add(RolePrueba)
        session.commit()  
         
        IdDpt = 21
        NameDpt = 'dptprobando2'
        DptPrueba = model.Dpt(IdDpt, NameDpt)         
        session.add(DptPrueba)
        session.commit() 
        
        Fullname = 'Joel Rivas'
        Username = 'Hiruma'
        Password = 'joelrivas'
        Email = 'rivasjoel@gmail.com'
        Iddpt = 21
        Idrole = 21
        UsuarioPrueba = model.User(Fullname, Username, Password, Email, IdDpt,IdRole)  
        session.add(UsuarioPrueba)
        session.commit()      
           
        self.assertFalse(auxUser.insertar('Joel Rivas','Hiruma32','joelriva34s','rivas34joel@gmail.com',21,21),"Correcto")  


        
     # test 4: Se inserta el usuario con fullname entero.   
    def test4insertar(self):
        self.limpiarBaseDeDatos() 
        auxUser = clsUser()       
        
        IdRole = 21
        NameRole = 'rolprobando2'
        RolePrueba = model.Role(IdRole, NameRole)     
        session.add(RolePrueba)
        session.commit()  
         
        IdDpt = 21
        NameDpt = 'dptprobando2'
        DptPrueba = model.Dpt(IdDpt, NameDpt)         
        session.add(DptPrueba)
        session.commit() 
           
        self.assertFalse(auxUser.insertar(3433,'Hiruma','joelrivas','rivasjoel@gmail.com',21,21),"Correcto")
       
        
    ### CASOS MALICIOSOS   
    # test 5: Se inserta el usuario violando las restricciones de las claves foraneas  y la base de datos esta vacia  
    def test5insertar(self): 
        self.limpiarBaseDeDatos() 
        auxUser = clsUser()       
                 
        self.assertFalse(auxUser.insertar('Joel Rivas','Hiruma','joelrivas','rivasjoel@gmail.com',21,21),"Correcto")
        
        # FUNCION MODIFICAR
    ###CASOS FRONTERAS O DE DOMINIO    
    # test 6: Se quiere modificar un usuario con la base de datos de Usuario vacia.
    def test6modificar(self):
        auxUser = clsUser()              
        IdRole = 21       
        IdDpt = 21
              
        self.assertFalse(auxUser.modificar('Joel Rivas','Hiruma','joelrivas','rivasjoel@gmail.com',IdRole,IdDpt),"Correcto")
     
    '''    
    # test 7: Se modifica un usuario en la base de datos.
    def test7modificar(self):
        auxUser = clsUser()  
                
        IdRole = 213
        NameRole = 'rolprobzando2'
        RolePrueba2 = model.Role(IdRole, NameRole)     
        session.add(RolePrueba2)
        session.commit()  
         
        IdDpt = 213
        NameDpt = 'dptprobazndo2'
        DptPrueba2 = model.Dpt(IdDpt, NameDpt)         
        session.add(DptPrueba2)
        session.commit() 
        
        Fullname = 'Joel Rivas'
        Username = 'Hiruma'
        Password = 'joelrivas'
        Email = 'rivasjoel@gmail.com'
        UsuarioPrueba = model.User(Fullname, Username, Password, Email, IdDpt,IdRole)  
        session.add(UsuarioPrueba)
        session.commit()      
          
        self.assertTrue(auxUser.modificar('Joel Rivas','Hirumax','joevtlrivas','rivasjoel@gmail.com',213,213),"Correcto")
         
      '''         