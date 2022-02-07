import uuid

class Producto:
    def __init__(self, nombre, categoria, inventario, descripcion, uid=None):
        self.nombre = nombre
        self.categoria = categoria
        self.inventario = inventario
        self.descripcion = descripcion
        self.uid = uid or uuid.uuid4()
        
    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return ['nombre', 'categoria', 'inventario', 'descripcion', 'uid']