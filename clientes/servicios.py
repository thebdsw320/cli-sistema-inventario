import csv
from clientes.modelos import Cliente
import os

class ServiciosCliente:
    def __init__(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla
    
    def crear_cliente(self, cliente):
        with open(self.nombre_tabla, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Cliente.schema())
            writer.writerow(cliente.to_dict())
    
    def listar_clientes(self):
        with open(self.nombre_tabla, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Cliente.schema())
            
            return list(reader)
    
    def actualizar_cliente(self, cliente_actualizado):
        clientes = self.listar_clientes()
        
        clientes_actualizados = []
        for cliente in clientes:
            if cliente['uid'] == cliente_actualizado.uid:
                clientes_actualizados.append(cliente_actualizado.to_dict())
            else:
                clientes_actualizados.append(cliente)
        
        self._guardar_en_disco(clientes_actualizados)
    
    def borrar_cliente(self, cliente_borrado):
        clientes = self.listar_clientes()
        
        for cliente in clientes:
            if cliente['uid'] == cliente_borrado.uid:
                clientes.remove(cliente)
                break
            
        self._guardar_en_disco(clientes)
    
    def _guardar_en_disco(self, clientes):
        tabla_temporal = self.nombre_tabla + '.tmp'
        with open(tabla_temporal, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Cliente.schema())
            writer.writerows(clientes)
        
        os.remove(self.nombre_tabla)
        os.rename(tabla_temporal, self.nombre_tabla)