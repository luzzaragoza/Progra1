# --- IMPORTS ---
from Inquilinos.datos import encabezado_inquilinos, inquilinos as matriz_inquilinos
from Inquilinos.crear import crear_matriz_inquilinos
from Inquilinos.modificar import modificar_inquilino
from Inquilinos.busqueda import busqueda_inquilino

from Propiedades.datos import encabezados_propiedades, propiedades as matriz_propiedades
from Propiedades.modificar import modificar_propiedad
from Propiedades.busqueda import busqueda_propiedad  
from Propiedades.crear import crear_cant_propiedades as crear_matriz_propiedades
from Propiedades.mostrar import mostrar_propiedades

from Contratos.datos import encabezados_contratos, contratos as matriz_contratos
from Contratos.crear import crear_matriz_contrato

from Pagos.datos import encabezados_pagos, pagos as matriz_pagos
from Pagos.crear import crear_matriz_pagos
from Pagos.modificar import modificar_pago

from FuncAux.mostrar import mostrar_matriz
from FuncAux.login import iniciar_sesion
from FuncAux.validaciones import parse_int, nonempty, norm   # <- lambdas/funcs de validación

from Usuarios.crear import crear_cant_usuario
from Usuarios.modificar import cambiar_contrasenia as modificar_usuario
from Usuarios.mostrar import mostrar_usuarios

from estadistica.estadisticas import mostrar_resumen


# --------- helpers genéricos (con lambdas/funcs) ----------
def pedir_cantidad(msg):
    """Pide un entero positivo (usa parse_int del módulo de validaciones)."""
    while True:
        n = parse_int(input(msg))
        if n is not None and n > 0:
            return n
        print("Ingrese un número entero positivo.\n")

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
def gestion_inqiuilinos():
    items = [
        ("1", "Crear Inquilinos",         lambda: matriz_inquilinos.extend(
            crear_matriz_inquilinos(pedir_cantidad("¿Cuántos inquilinos desea crear? "))
        )),
        ("2", "Mostrar Inquilinos",       lambda: mostrar_matriz(encabezado_inquilinos, matriz_inquilinos[0:])),
        ("3", "Modificar Inquilinos",     lambda: modificar_inquilino(matriz_inquilinos[0:])),
        ("4", "Buscar Inquilinos",        lambda: busqueda_inquilino(matriz_inquilinos)),
        ("5", "Resumen Estadístico",      lambda: mostrar_resumen(matriz_propiedades, matriz_contratos)),
        ("6", "Volver",                   lambda: None),
    ]
    menu_loop("Gestión de Inquilinos", items)

def gestion_propiedades():
    items = [
        ("1", "Crear Propiedades",   lambda: crear_matriz_propiedades(pedir_cantidad("¿Cuántas propiedades desea crear? "))),
        ("2", "Mostrar Propiedades", lambda: mostrar_propiedades()),
        ("3", "Modificar Propiedades", lambda: modificar_propiedad()),
        # Si tu busqueda_propiedad YA está adaptada a dict, llamala sin args:
        ("4", "Buscar Propiedades",  lambda: busqueda_propiedad()),
        ("5", "Volver",              lambda: None),
    ]
    menu_loop("Gestión de Propiedades", items)

def gestion_contratos():
    items = [
        ("1", "Crear Contratos", lambda: matriz_contratos.extend(
            crear_matriz_contrato(pedir_cantidad("¿Cuántos contratos desea crear? "))
        )),
        ("2", "Mostrar Contratos", lambda: mostrar_matriz(
            encabezados_contratos, matriz_contratos[0:], pos_mil={5}, censurar={1, 2}
        )),
        ("3", "Volver", lambda: None),
    ]
    menu_loop("Gestión de Contratos", items)

def gestion_pagos():
    items = [
        ("1", "Crear Pagos", lambda: matriz_pagos.extend(
            crear_matriz_pagos(pedir_cantidad("¿Cuántos pagos desea crear? "))
        )),
        ("2", "Mostrar Pagos", lambda: mostrar_matriz(encabezados_pagos, matriz_pagos[0:], pos_mil={3})),
        ("3", "Modificar Pagos", lambda: modificar_pago(matriz_pagos[0:])),
        ("4", "Volver", lambda: None),
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
        ("1", "Gestión de Inquilinos",  gestion_inqiuilinos),
        ("2", "Gestión de Propiedades", gestion_propiedades),
        ("3", "Gestión de Contratos",   gestion_contratos),
        ("4", "Gestión de Pagos",       gestion_pagos),
        ("5", "Gestión de Usuarios",    gestion_usuarios),
        ("6", "Resumen Estadístico",    lambda: mostrar_resumen(matriz_propiedades, matriz_contratos)),
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
