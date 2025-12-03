import json
import os

def cargar_json(modulo, archivo=None):
    if archivo is None:
        archivo = f"datos_{modulo.lower()}.json"
    ruta = f'{modulo}/{archivo}'
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta} está mal formateado.")
        return {}
    
def cargar_inquilinos():
    ruta = 'Inquilinos/datos_inquilino.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def cargar_propiedades():
    ruta = 'Propiedades/datos_propiedad.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def cargar_contratos():
    ruta = 'Contratos/datos_contrato.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

# --- IMPORTS ---
from Inquilinos.crear_inquilino import crear_cant_inquilinos
from Inquilinos.modificar_inquilino import modificar_inquilino
from Inquilinos.busqueda_inquilino import buscar_inquilinos as busqueda_inquilino
from Inquilinos.mostrar_inquilino import mostrar_inquilinos
from Inquilinos.baja_inquilino import baja_inquilino
from Inquilinos.busqueda_inquilino import menu_busqueda_inquilino

from Propiedades.modificar_propiedad import modificar_propiedad
#from Propiedades.busqueda_propiedad import busqueda_propiedad  
from Propiedades.crear_propiedad import crear_cant_propiedades
from Propiedades.mostrar_propiedad import mostrar_propiedades
from Propiedades.baja_propiedad import baja_propiedad
from Propiedades.tipos_propiedades import baja_tipo_propiedad

from Contratos.crear_contrato import crear_cant_contratos
from Contratos.modificar_contrato import modificar_estado_contrato
from Contratos.mostrar_contrato import mostrar_contratos

from Pagos.crear_pago import crear_cant_pagos
from Pagos.mostrar_pago import mostrar_pagos
from Pagos.tipos_pagos import devuelve_nombre_tipo as tipo_pago
from Pagos.tipos_pagos import baja_tipo_pago

from FuncAux.login import iniciar_sesion
from FuncAux.validaciones import parse_int, nonempty, norm
from FuncAux.estadistica import total_por_metodo, mostrar_resumen
from FuncAux.busqueda_relacionada import busqueda_relacionada_inq

from Usuarios.crear_usuario import crear_cant_usuario
from Usuarios.modificar_usuario import cambiar_contrasenia as modificar_usuario
from Usuarios.mostrar_usuario import mostrar_usuarios

inquilinos = cargar_inquilinos()
propiedades = cargar_propiedades()
contratos = cargar_contratos()


# --------- helpers genéricos (con lambdas/funcs) ----------
def pedir_cantidad(msg):
    """Pide un entero positivo (usa parse_int del módulo de validaciones)."""
    while True:
        n = parse_int(input(msg))
        if n is not None and n > 0:
            return n
        print("Ingrese una cantidad valida.\n")

def menu_loop(titulo, items):
    """
    items: lista de tuplas (clave, etiqueta, funcion_sin_args)
    Muestra el menú, despacha por lambda y vuelve al menú principal al elegir 'Volver/Salir'.
    """
    while True:
        print(f"----- {titulo} -----")
        for k, label, _ in items:
            print(f"{k}. {label}")
        opcion = input("Seleccione una opción: ").strip()

        # despachador
        encontrado = False
        for k, label, fn in items:
            if opcion == k:
                encontrado = True
                resultado = fn()
                # Si la etiqueta dice Volver/Salir, volvemos
                if label.lower().startswith(("volver", "salir")):
                    return resultado
                break
        if not encontrado:
            print("Opción no válida. Intente nuevamente.\n")


# --------- Menús específicos ----------
def gestion_inquilinos():
    items = [
        ("1", "Crear Inquilinos",         lambda: crear_cant_inquilinos(pedir_cantidad("¿Cuántos inquilinos desea crear? "))),
        ("2", "Mostrar Inquilinos",       lambda: mostrar_inquilinos()),
        ("3", "Modificar Inquilinos",     lambda: modificar_inquilino()),
        ("4", "Buscar Inquilinos",        lambda: menu_busqueda_inquilino(inquilinos=inquilinos, norm=norm, parse_int=parse_int)),
        ("5", "Buscar Contratos por Inquilino", lambda: busqueda_relacionada_inq(propiedades=propiedades, contratos=contratos, inquilinos=inquilinos)),
        ("6", "Baja de Inquilinos",       lambda: baja_inquilino()),
        ("7", "Volver",                   lambda: None),
    ]
    menu_loop("Gestión de Inquilinos", items)

def gestion_propiedades():
    items = [
        ("1", "Crear Propiedades",   lambda: crear_cant_propiedades(pedir_cantidad("¿Cuántas propiedades desea crear? "))),
        ("2", "Mostrar Propiedades", lambda: mostrar_propiedades()),
        ("3", "Modificar Propiedades", lambda: modificar_propiedad()),
        ("4", "Baja de Propiedades", lambda: baja_propiedad()),
        ("5", "Baja de Tipo de Propiedad", lambda: baja_tipo_propiedad()),
        ("6", "Volver",              lambda: None),
    ]
    menu_loop("Gestión de Propiedades", items)

def gestion_contratos():
    items = [
        ("1", "Crear Contratos", lambda:crear_cant_contratos(pedir_cantidad("¿Cuántos contratos desea crear? "))),
        ("2", "Mostrar Contratos", lambda: mostrar_contratos()),
        ("3", "Modificar Estado de Contrato", lambda: modificar_estado_contrato()),
        ("4", "Volver", lambda: None),
    ]
    menu_loop("Gestión de Contratos", items)

def gestion_pagos():
    items = [
        ("1", "Crear Pagos", lambda: crear_cant_pagos(pedir_cantidad("¿Cuántos pagos desea crear? "))),
        ("2", "Mostrar Pagos", lambda: mostrar_pagos()),
        ("3", "Total por Método de Pago", lambda: total_por_metodo(tipo_pago())),
        ("4", "Baja de Tipo de Pago", lambda: baja_tipo_pago()),  # Aquí podrías agregar la función correspondiente
        ("5", "Volver", lambda: None),
    ]
    menu_loop("Gestión de Pagos", items)

def gestion_usuarios():
    items = [
        ("1", "Crear Usuario(s)",     lambda: crear_cant_usuario(pedir_cantidad("¿Cuántos usuarios desea crear? "))),
        ("2", "Modificar contraseña", lambda: modificar_usuario()),
        ("3", "Mostrar Usuarios",     lambda: mostrar_usuarios()),
        ("4", "Volver",               lambda: None),
    ]
    menu_loop("Gestión de Usuarios", items)


# --------- Programa principal ----------
def menu():
    items = [
        ("1", "Gestión de Inquilinos",  gestion_inquilinos),
        ("2", "Gestión de Propiedades", gestion_propiedades),
        ("3", "Gestión de Contratos",   gestion_contratos),
        ("4", "Gestión de Pagos",       gestion_pagos),
        ("5", "Gestión de Usuarios",    gestion_usuarios),
        ("6", "Resumen Estadístico",    lambda: mostrar_resumen()),
        ("7", "Salir",                  lambda: None),
    ]
    menu_loop("Menú de Gestión de Alquileres", items)

def iniciar_sistema():
    print("----- Bienvenido al sistema -----")
    while not iniciar_sesion():
        pass
    menu()

# --- EJECUCIÓN ---
if __name__ == "__main__":
    iniciar_sistema()
