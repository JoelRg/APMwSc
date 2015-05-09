'''
Created on 8/5/2015

@author: joel
'''

import uuid
import hashlib
import re 
 
class clsLogin(object):
    
    def __init__(self):
        self.expRegular = ('(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                          '(([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d)|'
                          '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                          '(([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*[@.#$+*])|'
                          '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*\d([0-9a-zA-Z]|[@.#$+*])*[A-Z])|'
                          '(([0-9a-zA-Z]|[@.#$+*])*[@.#$+*]([0-9a-zA-Z]|[@.#$+*])*[A-Z]([0-9a-zA-Z]|[@.#$+*])*\d)')
        
         
    def encript(self, value):
        
        oHash=""
        olength_password=self.length_password(value)
        
        #Verifico el tamano
        
        if (olength_password >= 8 and olength_password<=16):
            esValida = re.search(self.expRegular ,value)
 
            if esValida: 
                # uuid es usado para generar numeros random
                salt = uuid.uuid4().hex
                # hash
                oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
     
        # ohash="" si no cumple con la longitud requerida o no es valida
        
        return oHash  

    
    def check_password(self, oPassworkEncript, oCheckPassword):
        # Verificar la longitud del password
        olength_password=self.length_password(oCheckPassword)
        if olength_password>=8 and olength_password<=16: 
            # uuid es usado para generar numeros random
            if oPassworkEncript == '':  #Si el oPassworkEncript es invalido
                return False
            oPassworkEncript, salt = oPassworkEncript.split(':')
            return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
        else:
            # El Password no posee la cantidad de caracteres requerida
            return False
    
    def length_password(self, user_password):
        # uuid es usado para generar numeros random
        return len(user_password)
