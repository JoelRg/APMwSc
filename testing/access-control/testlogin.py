'''
Created on 8/5/2015

@author: joel
'''

# Librerias a utilizar.

import os
import sys

# PATH que permite utilizar al modulo "login.py"
sys.path.append('../../business/access-control')
from login import clsLogin

import unittest

class TestLogin(unittest.TestCase):
    

    # VERIFICACION DE LA CLASE.
    
    # Test 1: Se crea el objeto clsLogin.
    
    def test1ObjectExist(self):
        auxLogin = clsLogin()
        self.assertIsNotNone(auxLogin)

    
    
    