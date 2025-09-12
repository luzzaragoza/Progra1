# --- IMPORTS ---
from Inquilinos.datos import matriz_inquilinos
from Inquilinos.crear import crear_matriz_inquilinos
from Inquilinos.modificar import modificar_inquilino
from Inquilinos.busqueda import busqueda_inquilino

from Propiedades.datos import matriz_propiedades
from Propiedades.crear import crear_matriz_propiedades
from Propiedades.modificar import modificar_propiedad
from Propiedades.busqueda import busqueda_propiedad

from Contratos.datos import matriz_contratos
from Contratos.crear import crear_matriz_contrato
from Contratos.modificar import modificar_contrato

from Pagos.datos import matriz_pagos
from Pagos.crear import crear_matriz_pagos
from Pagos.modificar import modificar_pago

from FuncAux.mostrar import mostrar_matriz
from FuncAux.login import validar_usuario, iniciar_sesion

from Usuarios.crear import crear_usuario
from Usuarios.modificar import modificar_usuario
#Funciones de Menu

def gestion_inqiuilinos():
    print("----- Gestión de Inquilinos -----")
    print("1. Crear Inquilinos")
    print("2. Mostrar Inquilinos")
    print("3. Modificar Inquilinos")
    print("4. Buscar Inquilinos")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        cant_inquilinos = int(input("¿Cuántos inquilinos desea crear? "))
        nuevos_inquilinos = crear_matriz_inquilinos(cant_inquilinos)
        matriz_inquilinos.extend(nuevos_inquilinos)
        print("Inquilinos creados exitosamente.")
    elif opcion == '2':
        mostrar_matriz(matriz_inquilinos[0], matriz_inquilinos[1:])
    elif opcion == '3':
        modificar_inquilino(matriz_inquilinos[1:])
    elif opcion == '4':
        busqueda_inquilino(matriz_inquilinos)
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_inqiuilinos()

def gestion_propiedades():
    print("----- Gestión de Propiedades -----")
    print("1. Crear Propiedades")
    print("2. Mostrar Propiedades")
    print("3. Modificar Propiedades")
    print("4. Buscar Propiedades")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        cant_propiedades = int(input("¿Cuántas propiedades desea crear? "))
        nuevas_propiedades = crear_matriz_propiedades(cant_propiedades)
        matriz_propiedades.extend(nuevas_propiedades)
        print("Propiedades creadas exitosamente.")
    elif opcion == '2':
        mostrar_matriz(matriz_propiedades[0], matriz_propiedades[1:])
    elif opcion == '3':
        modificar_propiedad(matriz_propiedades[1:])
    elif opcion == '4':
        busqueda_propiedad(matriz_propiedades[1:])
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_propiedades()

def gestion_contratos():
    print("----- Gestión de Contratos -----")
    print("1. Crear Contratos")
    print("2. Mostrar Contratos")
    print("3. Modificar Contratos")
    opcion = input("Seleccione una opción (1-3): ")
    if opcion == '1':
        cant_contratos = int(input("¿Cuántos contratos desea crear? "))
        nuevos_contratos = crear_matriz_contrato(cant_contratos)
        matriz_contratos.extend(nuevos_contratos)
        print("Contratos creados exitosamente.")
    elif opcion == '2':
        mostrar_matriz(matriz_contratos[0], matriz_contratos[1:])
    elif opcion == '3':
        modificar_contrato(matriz_contratos[1:])
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_contratos()

def gestion_pagos():
    print("----- Gestión de Pagos -----")
    print("1. Crear Pagos")
    print("2. Mostrar Pagos")
    print("3. Modificar Pagos")
    opcion = input("Seleccione una opción (1-3): ")
    if opcion == '1':
        cant_pagos = int(input("¿Cuántos pagos desea crear? "))
        nuevos_pagos = crear_matriz_pagos(cant_pagos)
        matriz_pagos.extend(nuevos_pagos)
        print("Pagos creados exitosamente.")

    elif opcion == '2':
        mostrar_matriz(matriz_pagos[0], matriz_pagos[1:])
    elif opcion == '3':
        modificar_pago(matriz_pagos[1:])
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_pagos()

def gestion_usuarios():
    print("----- Gestión de Usuarios -----")
    print("1. Crear Usuario")
    print("2. Modificar Usuario")
    opcion = input("Seleccione una opción (1-2): ")
    if opcion == '1':
        crear_usuario()
    elif opcion == '2':
        modificar_usuario()
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_usuarios()

#Programa principal

def menu():
    while True:
        print("----- Menú de Gestión de Alquileres -----")
        print("1. Gestión de Inquilinos")
        print("2. Gestión de Propiedades")
        print("3. Gestión de Contratos")
        print("4. Gestión de Pagos")
        print("5. Gestión de Usuarios")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == '1':
            gestion_inqiuilinos()
        elif opcion == '2':
            gestion_propiedades()
        elif opcion == '3':
            gestion_contratos()
        elif opcion == '4':
            gestion_pagos()
        elif opcion == '5':
            gestion_usuarios()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def iniciar_sistema():
    print("----- Bienvenido al sistema -----")
    
    # Solo permite entrar al menú si el login es correcto
    while not iniciar_sesion():
        pass  # sigue pidiendo login hasta que sea correcto

    # Una vez logueado, muestra el menú
    menu()

# --- EJECUCIÓN ---
iniciar_sistema()


import estadisticas 

def main():
    inmuebles = [
        {"id": 1, "estado": "ocupado", "valor": 120000},
        {"id": 2, "estado": "libre", "valor": 90000},
        {"id": 3, "estado": "ocupado", "valor": 150000}
    ]

    contratos = [
        {"mes": "Enero", "monto": 50000},
        {"mes": "Enero", "monto": 30000},
        {"mes": "Febrero", "monto": 40000}
    ]

    estadisticas.mostrar_resumen(inmuebles, contratos)

if __name__ == "__main__":
    main()
