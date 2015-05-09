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
    

    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsLogin.
    
    def test1ObjectExist(self):
        auxUser = clsUser()
        self.assertIsNotNone(auxUser)
        session.query(model.User).delete()  # Se limpia la base de datos.
        
        