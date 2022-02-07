import uuid

class Cliente:
    def __init__(self, nombre, compañia, email, posicion, uid=None):
        self.nombre = nombre
        self.compañia = compañia
        self.email = email
        self.posicion = posicion
        self.uid = uid or uuid.uuid4()
        
    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['nombre', 'compañia', 'email', 'posicion', 'uid']
    
    