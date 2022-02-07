import click
from clientes import comandos as cmd_cliente
from productos import comandos as cmd_productos

TABLA_CLIENTE = '.clientes.csv'
TABLA_PRODUCTO = '.productos.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['tabla_cliente'] = TABLA_CLIENTE
    ctx.obj['tabla_producto'] = TABLA_PRODUCTO
    
cli.add_command(cmd_cliente.all)
cli.add_command(cmd_productos.all)
    