
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
        
         
    def encriptar(self, value):
        
        oHash=""
        olength_password=self.longitud(value)
        
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
        olength_password=self.longitud(oCheckPassword)
        if olength_password>=8 and olength_password<=16: 
            # uuid es usado para generar numeros random
            if oPassworkEncript == '' or oPassworkEncript==None:  #Si el oPassworkEncript es invalido
                return False
            oPassworkEncript, salt = oPassworkEncript.split(':')
            return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
        else:
            # El Password no posee la cantidad de caracteres requerida
            return False
    
    def longitud(self, user_password):
        # uuid es usado para generar numeros random
        return len(user_password)
