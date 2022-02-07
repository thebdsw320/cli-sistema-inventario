import click
from clientes.servicios import ServiciosCliente
from clientes.modelos import Cliente
from tabulate import tabulate

@click.group()
def clientes():
    pass


@clientes.command()
@click.pass_context
def listar(ctx):
    """Lista todos los clientes"""
    servicio_cliente = ServiciosCliente(ctx.obj['tabla_cliente'])
    lista_clientes = servicio_cliente.listar_clientes()
    cabeceras = [campo.capitalize() for campo in Cliente.schema()]
    tabla = []
    
    for cliente in lista_clientes:
        tabla.append(
            [cliente['nombre'],
             cliente['compañia'],
             cliente['email'],
             cliente['posicion'],
             cliente['uid']])
    
    print(tabulate(tabla, cabeceras))


@clientes.command()
@click.option('-n', '--nombre',
              type=str,
              prompt=True,
              help='Nombre del cliente')
@click.option('-c', '--compañia',
              type=str,
              prompt=True,
              help='Compañia del cliente')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='Email del cliente')
@click.option('-p', '--posicion',
              type=str,
              prompt=True,
              help='Posición del cliente')
@click.pass_context
def crear(ctx, nombre, compañia, email, posicion):
    """Crea un nuevo cliente"""
    cliente = Cliente(nombre, compañia, email, posicion)
    servicio_cliente = ServiciosCliente(ctx.obj['tabla_cliente'])
    
    servicio_cliente.crear_cliente(cliente)


@clientes.command()
@click.argument('uid_cliente',
                type=str)
@click.pass_context
def actualizar(ctx, uid_cliente):
    """Actualiza un cliente"""
    servicio_cliente = ServiciosCliente(ctx.obj['tabla_cliente'])
    
    lista_clientes = servicio_cliente.listar_clientes()
    
    cliente = [cliente for cliente in lista_clientes if cliente['uid'] == uid_cliente]

    if cliente:
        cliente = _actualizar_flujo_cliente(Cliente(**cliente[0]))
        servicio_cliente.actualizar_cliente(cliente)
        
        click.echo('Cliente actualizado')
    else:
        click.echo('Cliente no encontrado')


def _actualizar_flujo_cliente(cliente):
    click.echo('Dejalo vacío si no quieres modificar ningún valor')
    
    cliente.nombre = click.prompt('Nuevo nombre', type=str, default=cliente.nombre)
    cliente.compañia = click.prompt('Nueva', type=str, default=cliente.compañia)
    cliente.email = click.prompt('Nuevo email', type=str, default=cliente.email)
    cliente.posicion = click.prompt('Nueva posicion', type=str, default=cliente.posicion)

    return cliente

@clientes.command()
@click.argument('uid_cliente',
                type=str)
@click.pass_context    
def borrar(ctx, uid_cliente):
    """Borra un cliente"""
    servicio_cliente = ServiciosCliente(ctx.obj['tabla_cliente'])
    lista_clientes = servicio_cliente.listar_clientes()
    cliente = [cliente for cliente in lista_clientes if cliente['uid'] == uid_cliente]
    
    if cliente:
        cliente_a_borrar = _borrar_flujo_cliente(Cliente(**cliente[0]))
        
        if cliente_a_borrar:
            servicio_cliente.borrar_cliente(cliente_a_borrar)
            click.echo('El cliente ha sido borrado exitosamente')
    else:
        click.echo('Cliente no encontrado, revise el UID')
        

def _borrar_flujo_cliente(cliente):
    click.echo(f'El cliente con el UID {cliente.uid} será eliminado')
    
    confirmacion = click.prompt(
        '¿Estás segura(o) de querer borrar al cliente? [y]/N', type=str, default='Y')

    if confirmacion.upper() == 'Y':
        return cliente
    
all = clientes
