import csv
from productos.modelos import Producto
import os
from click import echo

class ServiciosProducto:
    def __init__(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla
        
    def crear_producto(self, producto):
        with open(self.nombre_tabla, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Producto.schema())
            writer.writerow(producto.to_dict())
            
    def listar_productos(self):
        with open(self.nombre_tabla, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Producto.schema())
            
            return list(reader)
        
    def actualizar_producto(self, producto_actualizado):
        productos = self.listar_productos()
        
        productos_actualizados = []
        for producto in productos:
            if producto['uid'] == producto_actualizado.uid:
                productos_actualizados.append(producto_actualizado.to_dict())
            else:
                productos_actualizados.append(producto)
        
        self._guardar_en_disco(productos_actualizados)
        
    def borrar_producto(self, producto_borrado):
        productos = self.listar_productos()
        
        for producto in productos:
            if producto['uid'] == producto_borrado.uid:
                productos.remove(producto)
                break
        
        self._guardar_en_disco(productos)
    
    def vender_producto(self, producto_vendido):
        self.actualizar_producto(producto_vendido)           
        
    def _guardar_en_disco(self, productos):
        tabla_temporal = self.nombre_tabla + '.tmp'
        with open(tabla_temporal, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=Producto.schema())
            writer.writerows(productos)
        
        os.remove(self.nombre_tabla)
        os.rename(tabla_temporal, self.nombre_tabla)    