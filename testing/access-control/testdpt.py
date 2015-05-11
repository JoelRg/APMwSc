'''
Created on 8/5/2015

@author: joel
'''

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "login.py"
sys.path.append('../../business/access-control')
from dpt import clsDpt, session

# PATH que permite utilizar al modulo "model.py"
sys.path.append('../../data')
import model

import unittest

class TestDpt(unittest.TestCase):
    

    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsLogin.
    
    def test1ObjectExist(self):
        auxDpt = clsDpt()
        self.assertIsNotNone(auxDpt)
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        
        