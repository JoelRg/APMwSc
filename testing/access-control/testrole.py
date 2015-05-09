'''
Created on 8/5/2015

@author: joel
'''

# Librerias a utilizar.

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
    
    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsRole.
    
    def test1ObjectExist(self):
        auxRole = clsRole()
        self.assertIsNotNone(auxRole)
        session.query(model.Role).delete()  # Se limpia la base de datos.
    
    
    
    