import os
import sys

# PATH que permite utilizar al modulo "dpt.py"
sys.path.append('../../business/access-control')
from dpt import clsDpt, session

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

import unittest

class TestDpt(unittest.TestCase):

    # Test 1: Se crea el objeto clsDpt.
    def test1_ObjectExist(self):
        temp = clsDpt()
        self.assertIsNotNone( temp )
        session.query( model.Dpt ).delete()  # Se limpia la base de datos.

    ### FUNCION BUSCAR ###

    # Test 2: Buscar el id de un dpt que exista. 
    def test2_buscarExist(self):
        session.query( model.Dpt ).delete()
        nuevoIdDpt = 1
        nuevoNameDpt = 'dptprueba'
        newDpt = model.Dpt(nuevoIdDpt, nuevoNameDpt) 
        session.add(newDpt)
        session.commit()   
        
        temp = clsDpt()
        idDpt = 1
        query = temp.buscar( idDpt )
        self.assertIsNotNone( query[0] )
    
    # Test 3: Buscar el id de un dpt que no exista.
    def test3_buscarNotExist(self):
        temp = clsDpt()
        idDpt = 1000
        query = temp.buscar( idDpt )
        self.assertEqual(query,[])
    
    # Test 4: El id del dpt a buscar es un string.
    def test4_buscarString(self):
        temp = clsDpt()
        idDpt = '1'
        query = temp.buscar( idDpt )
        self.assertEqual(query,[])
    
    # Test 5: El id del dpt a buscar es de tipo float.
    def test5_buscarFloat(self):
        temp = clsDpt()
        idDpt = 1.01
        query = temp.buscar( idDpt )
        self.assertEqual(query,[])  

    # Test 6: El id del dpt a buscar es nulo.
    def test6_buscarNone(self):
        temp = clsDpt()
        idDpt = None
        query = temp.buscar( idDpt )
        self.assertEqual(query,[]) 


    ### FUNCION INSERTAR ###

    # Test 8: Insertar un dpt que ya existe.
    def test8_insertarExist(self):
        temp = clsDpt()
        idDpt = 2
        nameDpt = 'dpt'
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)
        
    # Test 9: El id del dpt a insertar no existe pero el nombre si.
    def test9_insertarIdNotExistNameExist(self):
        temp = clsDpt()
        idDpt = 20
        nameDpt = 'dpt'
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)
        
    # Test 10: El id del dpt a insertar existe pero el nombre no.
    def test10_insertarIdExistNameNotExist(self):
        temp = clsDpt()
        idDpt = 2
        nameDpt = 'dpto'
        DptPrueba = model.Dpt(idDpt, nameDpt)         
        session.add(DptPrueba)
        session.commit() 
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)

    # Test 11: El id del dpt a insertar es valido pero el nombre es 
    #          la cadena vacia.
    def test11_insertarIdNotExistNameLen0(self):
        temp = clsDpt()
        idDpt = 25
        nameDpt = ''
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertTrue(resultado)

    # Test 12: El id del dpt a insertar es valido pero el nombre es
    #          una cadena de 51 caracteres.
    def test12_insertarIdNotExistNameLen51(self):
        temp = clsDpt()
        idDpt = 25
        nameDpt = 'r'*51
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)

    # Test 13: El id del dpt a insertar es valido pero el nombre es 
    #          un numero.
    def test13_insertarIdNotExistNameNumber(self):
        temp = clsDpt()
        idDpt = 25
        nameDpt = 123456
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)

    # Test 14: El id del dpt a insertar es un numero negativo.
    def test14_insertarIdNegative(self):
        temp = clsDpt()
        idDpt = -25
        nameDpt = 'dpto'
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)
        
    # Test 15: El id del dpt a insertar es un string.
    def test15_insertarIdString(self):
        temp = clsDpt()
        idDpt = '25'
        nameDpt = 'dpto'
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)
        
    # Test 16: El id del dpt a insertar es un float.
    def test16_insertarIdFloat(self):
        temp = clsDpt()
        idDpt = 25.01
        nameDpt = 'dpto'
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)
 
    # Test 17: El id del dpt a insertar es None.
    def test17_insertarIdNone(self):
        temp = clsDpt()
        idDpt = None
        nameDpt = 'dpto'
        resultado = temp.insertar( idDpt, nameDpt )
        self.assertFalse(resultado)

    ### FUNCION MODIFICAR ###

    # Test 18: El id del dpt a modificar existe en la base de datos y el
    #          nuevo nombre se encuentra disponible.
    def test18_modificarIdExistNewNameAvailable(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida.
        newIdDpt = 3
        newNameDpt = 'dptDePrueba1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        temp = clsDpt()
        idDpt = 3
        newNameDpt = 'dptDePruebaX'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado )         
    
    # Test 19: El id del dpt a modificar existe en la base de datos y el
    #          nuevo nombre no se encuentra disponible.
    def test19_modificarIdExistNewNameNoAvailable(self):
        temp = clsDpt()
        idDpt = 3
        newNameDpt = 'dptDePruebaX'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado )  
    
    # Test 20: El id del dpt a modificar no existe en la base de datos 
    #          pero el nuevo nombre se encuentra disponible.
    def test20_modificarIdNoExistNewNameAvailable(self):
        temp = clsDpt()
        idDpt = 20
        newnameDpt = 'dptDePruebaX2'
        resultado = temp.modificar( idDpt, newnameDpt )
        self.assertFalse( resultado ) 
    
    # Test 21: El id del dpt a modificar no existe en la base de datos 
    #          y el nuevo nombre no se encuentra disponible.
    def test21_modificarIdNoExistNewNameNoAvailable(self):
        temp = clsDpt()
        idDpt = 20
        newNameDpt = 'dptDePruebaX'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )  
    
    # Test 22: El id del dpt a modificar existe en la base de datos y su
    #          valor es igual a 1. El nuevo nombre se encuentra disponible.
    def test22_modificarIdExistIqual1NewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdDpt = 1
        newNameDpt = 'dptPruebaCaso1'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 
        
        temp = clsDpt()
        idDpt = 1
        newNameDpt = 'dptDePruebaX3'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado ) 

    # Test 23: El id del dpt a modificar existe en la base de datos y su
    #          valor es un numero muy grande. El nuevo nombre se encuentra disponible.     
    def test23_modificarIdExistIqualBigNumberNewNameAvailable(self):
        # Se inserta un elemento en la base. Dicha insercion se asegura
        # que es valida. 
        newIdDpt = (2**31)-1
        newNameDpt = 'dptDePruebaCasoBig'
        newDpt = model.Dpt(newIdDpt, newNameDpt) 
        session.add(newDpt)
        session.commit() 

        temp = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'dptDePruebaXBig'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado )  
    
    # Test 24: El id del dpt a modificar existe en la base de datos. El nuevo 
    #          nombre se encuentra disponible y es de largo 1.
    def test24_modificarIdExistNewNameAvailableLen1(self):
        temp = clsDpt()
        idDpt = 3
        newNameDpt = '1'
        DptPrueba = model.Dpt(idDpt, "algo")         
        session.add(DptPrueba)
        session.commit() 
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado )   
    
    # Test 27: El id del dpt a modificar existe en la base de datos y su valor es
    #          igual a 1. El nuevo nombre es valido y su longitud es igual a 50.
    def test27_modificarIdExistIqual1NewNameAvailableLen50(self):
        temp = clsDpt()
        idDpt = 1
        newNameDpt = 'b'*50
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado ) 
            
    # Test 28: El id del dpt a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 1.
    def test28_modificarIdExistIqualBigNumberNewNameAvailableLen1(self):
        temp = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'a'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado ) 

    # Test 29: El id del dpt a modificar existe en la base de datos y su valor es
    #          un numero muy grande. El nuevo nombre es valido y su longitud es igual a 50.
    def test29_modificarIdExistIqualBigNumberNewNameAvailableLen50(self):
        temp = clsDpt()
        idDpt = (2**31)-1
        newNameDpt = 'a'*50
        resultado= temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado ) 

    # Test 30: El id dado del dpt a modificar es un string.
    def test30_modificarIdString(self):        
        temp = clsDpt()
        idDpt = '1'
        newNameDpt = 'dptprueba'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )    
        
    # Test 31: El id dado del dpt a modificar es un numero negativo.    
    def test31_modificarIdNegative(self):        
        temp = clsDpt()
        idDpt = -1
        newNameDpt = 'dptprueba'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )   

    # Test 32: El id dado del dpt a modificar es un float.
    def test32_modificarIdFloat(self):        
        temp = clsDpt()
        idDpt = 1.0
        newNameDpt = 'dptprueba'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )   
        
    # Test 33: El id dado del dpt a modificar es None.         
    def test33_modificarIdNone(self):        
        temp = clsDpt()
        idDpt = None
        newNameDpt = 'dptprueba'
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )   
    
    # Test 34: El nuevo nombre para el dpt a modificar es un string vacio.
    def test34_modificarNewNameIsEmpty(self):        
        temp = clsDpt()
        idDpt = 1
        newNameDpt = ''
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertTrue( resultado )    
        
    # Test 35: El nuevo nombre para el dpt a modificar es de longitu 51.    
    def test35_modificarNewNameLen51(self):        
        temp = clsDpt()
        idDpt = 1
        newNameDpt = 'c'*51
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )   

    # Test 36: El nuevo nombre para el dpt a modificar es un numero.
    def test36_modificarNewNameIsNumber(self):        
        temp = clsDpt()
        idDpt = 1
        newNameDpt = 12345
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )   
        
    # Test 37: El nuevo nombre para el dpt a modificar es None. 
    def test37_modificarNewNameNone(self):        
        temp = clsDpt()
        idDpt = 1
        newNameDpt = None
        resultado = temp.modificar( idDpt, newNameDpt )
        self.assertFalse( resultado )  


    ### FUNCION ELIMINAR ###


    # Test 39: El dpt a eliminar no existe en la base de datos.
    def test39_eliminarNoExist(self):
        
        temp = clsDpt()
        idDpt = (2**31)-1
        resultado = temp.eliminar( idDpt )
        self.assertFalse( resultado )
        
    # Test 40: El id del dpt a eliminar es un string.
    def test40_eliminarIdString(self):
        temp = clsDpt()
        idDpt = '1'
        resultado = temp.eliminar( idDpt )
        self.assertFalse( resultado )
    
    # Test 41: El id del dpt a eliminar es un float.
    def test41_eliminarIdFloat(self):
        temp = clsDpt()
        idDpt = 1.01
        resultado = temp.eliminar( idDpt )
        self.assertFalse( resultado ) 

    # Test 42: El id del dpt a eliminar es None.
    def test42_eliminarIdNone(self):
        temp = clsDpt()
        idDpt = None
        resultado = temp.eliminar( idDpt )
        self.assertFalse( resultado )


