# Sistema de Ventas en una CLI (Command Line Interface) - CRUD en Python

## Requisitos
- Python >= 3.6 

## Instalación
1. Clona o descarga el repositorio:
    ```
    $ git clone https://github.com/thebdsw320/cli-sistema-inventario.git
    ```
2. Abre la terminal dentro del directorio del proyecto y crea un ambiente virtual
    ```bash
    $ python3 -m venv {NOMBRE-AMBIENTE-VIRTUAL}
    $ source {NOMBRE-AMBIENTE-VIRTUAL}/bin/activate
    ```
3. Instala la aplicación
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ pip install --editable .
    ```

## CRUD de Clientes
1. Listar clientes
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas clientes listar
    ```
2. Crear clientes
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas clientes crear
    ```
3. Actualizar clientes
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas clientes actualizar {UID_CLIENTE}
    ```
4. Borrar clientes
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas clientes borrar {UID_CLIENTE}
    ```

## CRUD de Productos (Inventario)
1. Listar productos
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas productos listar
    ```
2. Crear productos
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas productos crear
    ```
3. Actualizar productos
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas productos actualizar {UID_PRODUCTO}
    ```
4. Borrar productos
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas productos borrar {UID_PRODUCTO}
    ```
5. Vender productos
    ```bash
    ({NOMBRE-AMBIENTE-VIRTUAL}) $ ventas productos vender {UID_PRODUCTO} {CANTIDAD}
    ```
