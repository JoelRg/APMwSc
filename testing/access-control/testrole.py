

import os
import sys

# PATH que permite utilizar al modulo "role.py"
sys.path.append('../../business/access-control')
from role import clsRole, session

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

import unittest

class TestRole(unittest.TestCase):
    
    def limpiarBaseDeDatos(self):
        # Se limpia la base de datos.      
        session.query(model.User).delete()
        session.query(model.Dpt).delete() 
        session.query(model.Role).delete() 
    
    
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsRole.
    def test_1_ObjectExist(self):
        temp = clsRole()
        self.assertIsNotNone(temp)
        session.query(model.Role).delete()    # Se limpia la base de datos.


    ### FUNCION BUSCAR ###

    # Test 2: Buscar el id de un rol que exista. 
    def test_2_buscar_idRoleExist(self):
        session.query(model.Role).delete()
        tempIdRole = 1
        tempNameRole = 'role1'
        tempRole = model.Role(tempIdRole, tempNameRole) 
        session.add(tempRole)
        session.commit()   
        
        tmpRole = clsRole()
        idRole = tempIdRole
        query = tmpRole.buscar(idRole)
        self.assertNotEquals(query,[])
    
    # Test 3: Buscar el id de un rol que no exista.
    def test_3_buscarNotExist(self):
        tempRole = clsRole()
        idRole = 1000
        query = tempRole.buscar( idRole )
        self.assertEqual(query,[])
    
    # Test 4: El id del rol a buscar es un string.
    def test_4_buscarString(self):
        tempRole = clsRole()
        idRole = '1'
        query = tempRole.buscar( idRole )
        self.assertEqual(query,[])
    
    # Test 5: El id del rol a buscar es de tipo float.
    def test_5_buscarFloat(self):
        tempRole = clsRole()
        idRole = 1.01
        query = tempRole.buscar( idRole )
        self.assertEqual(query,[])  

    # Test 6: El id del rol a buscar es nulo.
    def test_6_buscarNone(self):
        tempRole = clsRole()
        idRole = None
        query = tempRole.buscar( idRole )
        self.assertEqual(query,[])

    ### FUNCION INSERTAR ###

    # Test 7: Insertar un rol que no existe.
    def test_7_insertarNoExist(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        idRole = 2
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertTrue(resultado)
    
    # Test 8: Insertar un rol que ya existe.
    def test_8_insertarExist(self):
        tempRole = clsRole()
        idRole = 2
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)
        
    # Test 9: El id del rol a insertar no existe pero el nombre si.
    def test_9_insertarIdNotExistNameExist(self):
        tempRole = clsRole()
        idRole = 20
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)
        
    # Test 10: El id del rol a insertar existe pero el nombre no.
    def test_10_insertarIdExistNameNotExist(self):
        tempRole = clsRole()
        idRole = 2
        nameRole = 'prueba'
        aux=model.Role(idRole,"algo")
        session.add(aux)
        session.commit()
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)

    # Test 11: El id del rol a insertar es un numero negativo.
    def test_11_insertarIdNegative(self):
        tempRole = clsRole()
        idRole = -25
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)
        
    # Test 12: El id del rol a insertar es un string.
    def test_12_insertarIdString(self):
        tempRole = clsRole()
        idRole = '25'
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)
        
    # Test 13: El id del rol a insertar es un flotante.
    def test_13_insertarIdFloat(self):
        tempRole = clsRole()
        idRole = 25.01
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)
 
    # Test 14: El id del rol a insertar es None.
    def test_14_insertarIdNone(self):
        tempRole = clsRole()
        idRole = None
        nameRole = 'prueba'
        resultado = tempRole.insertar( idRole, nameRole )
        self.assertFalse(resultado)

    ### FUNCION ELIMINAR ###

     # Test 15: El rol a eliminar existe en la base de datos.
    def test_15_eliminarExist(self):
        session.query(model.Role).delete()
        tempRole = clsRole()
        idRole = (2**31)-1
        aux=model.Role(idRole,"algo")
        session.add(aux)
        session.commit()
        resultado = tempRole.eliminar( idRole )
        self.assertTrue( resultado )

    # Test 16: El rol a eliminar no existe en la base de datos.
    def test_16_eliminarNoExist(self):
        tempRole = clsRole()
        idRole = (2**31)-1
        resultado = tempRole.eliminar( idRole )
        self.assertFalse( resultado )
        
    # Test 17: El id del rol a eliminar es un string.
    def test_17_eliminarIdString(self):
        tempRole = clsRole()
        idRole = '1'
        resultado = tempRole.eliminar( idRole )
        self.assertFalse( resultado )
    
    # Test 18: El id del role a eliminar es un float.
    def test_18_eliminarIdFloat(self):
        tempRole = clsRole()
        idRole = 1.01
        resultado = tempRole.eliminar( idRole )
        self.assertFalse( resultado ) 

    # Test 19: El id del role a eliminar es None.
    def test_19_eliminarIdNone(self):
        tempRole = clsRole()
        idRole = None
        resultado = tempRole.eliminar( idRole )
        self.assertFalse( resultado )

    # Test 20: El id del role a eliminar es un numero negativo.
    def test_20_eliminarIdNegative(self):
        tempRole = clsRole()
        idRole = -1
        resultado = tempRole.eliminar( idRole )
        self.assertFalse( resultado ) 

    ### FUNCION MODIFICAR ###

    # Test 21: El id del rol a modificar existe en la base de datos y el
    #          nuevo nombre se encuentra disponible.
    def test_21_modificarIdExistNewNameAvailable(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        newIdRole = 3
        newNameRole = 'prueba1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 
        
        tempRole = clsRole()
        idRole = newIdRole
        newNameRole = 'prueba2'
        resultado = tempRole.modificar(idRole, newNameRole)
        self.assertTrue(resultado)         
    
    # Test 23: El id del rol a modificar no existe en la base de datos 
    #          pero el nuevo nombre se encuentra disponible.
    def test_23_modificarIdNoExistNewNameAvailable(self):
        tempRole = clsRole()
        idRole = 20
        newNameRole = 'rolDePruebaX2'
        resultado = tempRole.modificar( idRole, newNameRole )
        self.assertFalse( resultado ) 
    
    # Test 24: El id del rol a modificar no existe en la base de datos 
    #          y el nuevo nombre no se encuentra disponible.
    def test_24_modificarIdNoExistNewNameNoAvailable(self):
        tempRole = clsRole()
        idRole = 20
        newNameRole = 'rolDePruebaX'
        resultado = tempRole.modificar( idRole, newNameRole )
        self.assertFalse( resultado )  

    # Test 25: El id del rol a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo nombre se encuentra disponible.
    def test_25_modificarIdExistIqual1NewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdRole = 1
        newNameRole = 'roleDePruebaCaso1'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 
        
        tempRole = clsRole()
        idRole = 1
        newNameRole = 'rolDePruebaX3'
        resultado= tempRole.modificar( idRole, newNameRole )
        self.assertTrue( resultado ) 

    # Test 26: El id del rol a modificar existe en la base de datos y su
    #          valor es un numero muy grande. El nuevo nombre se encuentra disponible.     
    def test_26_modificarIdExistIqualBigNumberNewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdRole = (2**31)-1
        newNameRole = 'roleDePruebaCasoBig'
        newRole = model.Role(newIdRole, newNameRole) 
        session.add(newRole)
        session.commit() 

        tempRole = clsRole()
        idRole = (2**31)-1
        newNameRole = 'rolDePruebaXBig'
        resultado = tempRole.modificar( idRole, newNameRole )
        self.assertTrue( resultado )  
    
    # Test 27: El id del rol a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 1.
    def test_27_modificarIdExistNewNameAvailableLen1(self):
        session.query(model.Role).delete()
        tempRole = clsRole()
        idRole = 3
        nameRole = '1'
        aux=model.Role(idRole,"algo")
        session.add(aux)
        session.commit()
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertTrue( resultado )  
    
    # Test 28: El id del rol a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 50.
    def test_28_modificarIdExistNewNameAvailableLen50(self):
        tempRole = clsRole()
        idRole = 4
        nameRole = 'x'*50
        aux=model.Role(idRole,"algo3")
        session.add(aux)
        session.commit()
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertTrue( resultado )  
    
    # Test 29: El id del rol a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 1.
    def test_29_modificarIdExistIqual1NewNameAvailableLen1(self):
        tempRole = clsRole()
        idRole = 1
        nameRole = 'z'
        aux=model.Role(idRole,"algo2")
        session.add(aux)
        session.commit()
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertTrue( resultado ) 
    
    # Test 30: El id del rol a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 50.
    def test_30_modificarIdExistIqual1NewNameAvailableLen50(self):
        session.query(model.Role).delete()
        tempRole = clsRole()
        idRole = 1
        nameRole = 'z'*50
        aux=model.Role(idRole,"algo")
        session.add(aux)
        session.commit()
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertTrue( resultado ) 
            
    # Test 31: El id del rol a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 1.
    
    def test_31_modificarIdExistIqualBigNumberNewNameAvailableLen1(self):
        tempRole = clsRole()
        idRole = (2**31)-1
        nameRole = 'y'
        aux=model.Role(idRole,"algo5")
        session.add(aux)
        session.commit()
        resultado = tempRole.modificar( idRole, "das" )
        self.assertTrue( resultado ) 

    # Test 32: El id del rol a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 50.
    def test_32_modificarIdExistIqualBigNumberNewNameAvailableLen50(self):
        session.query(model.Role).delete()
        idRole = (2**31)-1
        newNameRole = 'y'*49
        aux=model.Role(idRole,"algo")
        session.add(aux)
        session.commit()
        tempRole = clsRole()

        resultado = tempRole.modificar( idRole, newNameRole )
        self.assertTrue( resultado ) 

    ### CASOS INVALIDOS( Casos Malicia )
    # Test 33: El id dado del rol a modificar es un string.
    def test_33_modificarIdString(self):        
        tempRole = clsRole()
        idRole = '1'
        nameRole = 'prueba'
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )    
        
    # Test 34: El id dado del rol a modificar es un numero negativo.    
    def test_34_modificarIdNegative(self):        
        tempRole = clsRole()
        idRole = -1
        nameRole = 'prueba'
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )   

    # Test 35: El id dado del rol a modificar es un float.
    def test_35_modificarIdFloat(self):        
        tempRole = clsRole()
        idRole = 1.0
        nameRole = 'prueba'
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )   
        
    # Test 36: El id dado del rol a modificar es None.         
    def test_36_modificarIdNone(self):        
        tempRole = clsRole()
        idRole = None
        nameRole = 'prueba'
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )   
    
    # Test 37: El nuevo nombre para el rol a modificar es un string vacio.
    def test_37_modificarNewNameIsEmpty(self):        
        tempRole = clsRole()
        idRole = 1
        nameRole = ''
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )  

    # Test 38: El nuevo nombre para el rol a modificar es un numero.
    def test_38_modificarNewNameIsNumber(self):        
        tempRole = clsRole()
        idRole = 1
        nameRole = 12345
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )   
        
    # Test 39: El nuevo nombre para el rol a modificar es None. 
    def test_39_modificarNewNameNone(self):        
        tempRole = clsRole()
        idRole = 1
        nameRole = None
        resultado = tempRole.modificar( idRole, nameRole )
        self.assertFalse( resultado )  




