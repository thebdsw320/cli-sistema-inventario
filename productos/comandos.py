import click
from productos.servicios import ServiciosProducto
from productos.modelos import Producto
from tabulate import tabulate

@click.group()
def productos():
    pass


@productos.command()
@click.pass_context
def listar(ctx):
    """Lista todos los productos existentes"""
    servicios_producto = ServiciosProducto(ctx.obj['tabla_producto'])
    lista_productos = servicios_producto.listar_productos()
    cabeceras = [campo.capitalize() for campo in Producto.schema()]
    tabla = []
    
    for producto in lista_productos:
        tabla.append([
            producto['nombre'],
            producto['categoria'],
            producto['inventario'],
            producto['descripcion'],
            producto['uid']])
    
    print(tabulate(tabla, cabeceras))


@productos.command()
@click.option('-n', '--nombre',
              type=str,
              prompt=True,
              help='Nombre del  producto')
@click.option('-c', '--categoria',
              type=str,
              prompt=True,
              help='Categoria del  producto')
@click.option('-i', '--inventario',
              type=str,
              prompt=True,
              help='Inventario del producto')
@click.option('-d', '--descripcion',
              type=str,
              prompt=True,
              help='Descripción del  producto')
@click.pass_context
def crear(ctx, nombre, categoria, inventario, descripcion):
    """Crea un nuevo producto"""
    producto = Producto(nombre, categoria, inventario, descripcion)
    servicios_producto = ServiciosProducto(ctx.obj['tabla_producto'])
    
    servicios_producto.crear_producto(producto)
    

@productos.command()
@click.argument('uid_producto',
                type=str)
@click.pass_context
def actualizar(ctx, uid_producto):
    """Actualiza un producto"""
    servicios_producto = ServiciosProducto(ctx.obj['tabla_producto'])
    lista_productos = servicios_producto.listar_productos()
    
    producto = [producto for producto in lista_productos if producto['uid'] == uid_producto]
    
    if producto:
        producto = _actualizar_flujo_producto(Producto(**producto[0]))
        servicios_producto.actualizar_producto(producto)
        
        click.echo('Producto actualizado')
    else:
        click.echo(f'Producto con UID {uid_producto}')    

def _actualizar_flujo_producto(producto):
    click.echo(f'El producto con UID {producto.uid} será actualizado')
    click.echo('Si no quieres modificar nada, dejalo vacio')
    
    producto.nombre = click.prompt('Nuevo nombre', type=str, default=producto.nombre)
    producto.categoria = click.prompt('Nueva categoria', type=str, default=producto.categoria)
    producto.inventario = click.prompt('Nuevo inventario', type=str, default=producto.inventario)
    producto.descripcion = click.prompt('Nueva descripcion', type=str, default=producto.descripcion)
    
    return producto

@productos.command()
@click.argument('uid_producto',
                type=str)
@click.pass_context
def borrar(ctx, uid_producto):
    """Borra un producto"""
    servicio_producto = ServiciosProducto(ctx.obj['tabla_producto'])
    lista_productos = servicio_producto.listar_productos()
    producto = [producto for producto in lista_productos if producto['uid'] == uid_producto]
    
    if producto:
        producto_a_borrar = _borrar_flujo_producto(Producto(**producto[0]))
        
        if producto_a_borrar:
            servicio_producto.borrar_producto(producto_a_borrar)
            click.echo('El producto ha sido eliminado exitosamente')
        else:
            click.echo('Producto no encontrado, revise el UID')

def _borrar_flujo_producto(producto):
    click.echo(f'El producto con el UID {producto.uid} será borrado')
    
    confirmacion = click.prompt(
        '¿Estás segura(o) de querer borrar al producto? [y]/N', type=str, default='Y')
    
    if confirmacion.upper() == 'Y':
        return producto
    

@productos.command()
@click.argument('uid_producto',
                type=str)
@click.argument('cantidad',
                type=int)
@click.pass_context
def vender(ctx, uid_producto, cantidad):
    """Venta de productos"""
    servicios_producto = ServiciosProducto(ctx.obj['tabla_producto'])
    lista_productos = servicios_producto.listar_productos()
    producto = [producto for producto in lista_productos if producto['uid'] == uid_producto]
    
    if producto:
        producto_a_vender = _vender_flujo_producto(Producto(**producto[0]), cantidad)

        if producto_a_vender:
            servicios_producto.vender_producto(producto_a_vender)
            click.echo('Venta exitosa')
    else:
        click.echo('Algo ha salido mal...')
        

def _vender_flujo_producto(producto, cantidad):
    click.echo(f'Se venderán {cantidad} piezas del producto con UID {producto.uid}')
    
    confirmacion = click.prompt(
        '¿Confirmar transacción? [y]/N', type=str, default='Y')
    
    if confirmacion.upper() == 'Y':
        if int(producto.inventario) >= cantidad:
            producto.inventario = str(int(producto.inventario) - cantidad)
            return producto

all = productos