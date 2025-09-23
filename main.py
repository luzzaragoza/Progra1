# --- IMPORTS ---
from Inquilinos.datos import encabezado_inquilinos, inquilinos as matriz_inquilinos
from Inquilinos.crear import crear_matriz_inquilinos
from Inquilinos.modificar import modificar_inquilino
from Inquilinos.busqueda import busqueda_inquilino

from Propiedades.datos import encabezados_propiedades, propiedades as matriz_propiedades
from Propiedades.crear import crear_matriz_propiedades
from Propiedades.modificar import modificar_propiedad
from Propiedades.busqueda import busqueda_propiedad

from Contratos.datos import encabezados_contratos, contratos as matriz_contratos
from Contratos.crear import crear_matriz_contrato  

from Pagos.datos import encabezados_pagos, pagos as matriz_pagos
from Pagos.crear import crear_matriz_pagos
from Pagos.modificar import modificar_pago

from FuncAux.mostrar import mostrar_matriz
from FuncAux.login import iniciar_sesion

from Usuarios.crear import crear_cant_usuario
from Usuarios.modificar import cambiar_contrasenia as modificar_usuario
from Usuarios.mostrar import mostrar_usuarios

from estadistica.estadisticas import mostrar_resumen


#Funciones de Menu

def gestion_inqiuilinos():
    print("----- Gestión de Inquilinos -----")
    print("1. Crear Inquilinos")
    print("2. Mostrar Inquilinos")
    print("3. Modificar Inquilinos")
    print("4. Buscar Inquilinos")
    print("5. Resumen Estadístico")

    opcion = input("Seleccione una opción (1-5): ")
    if opcion == '1':
        cant_inquilinos = int(input("¿Cuántos inquilinos desea crear? "))
        nuevos_inquilinos = crear_matriz_inquilinos(cant_inquilinos)
        matriz_inquilinos.extend(nuevos_inquilinos)
        print("Inquilinos creados exitosamente.")
    elif opcion == '2':
        mostrar_matriz(encabezado_inquilinos, matriz_inquilinos[0:])
    elif opcion == '3':
        modificar_inquilino(matriz_inquilinos[0:])
    elif opcion == '4':
        busqueda_inquilino(matriz_inquilinos)
    elif opcion == '5':
        mostrar_resumen(matriz_propiedades, matriz_contratos)
    else:
        print("Opción no válida. Intente nuevamente.")
    gestion_inqiuilinos()

def gestion_propiedades():
    print("----- Gestión de Propiedades -----")
    print("1. Crear Propiedades")
    print("2. Mostrar Propiedades")
    print("3. Modificar Propiedades")
    print("4. Buscar Propiedades")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")
    if opcion == '1':
        cant_propiedades = int(input("¿Cuántas propiedades desea crear? "))
        nuevas_propiedades = crear_matriz_propiedades(cant_propiedades)
        matriz_propiedades.extend(nuevas_propiedades)
        print("Propiedades creadas exitosamente.")
    elif opcion == '2':
        mostrar_matriz(encabezados_propiedades, matriz_propiedades[0:], pos_mil={3})
    elif opcion == '3':
        modificar_propiedad(matriz_propiedades[0:])
    elif opcion == '4':
        busqueda_propiedad(matriz_propiedades[0:])
    elif opcion == '5':
            print("Saliendo al menu principal...")
            menu()
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_propiedades()

def gestion_contratos():
    print("----- Gestión de Contratos -----")
    print("1. Crear Contratos")
    print("2. Mostrar Contratos")
    print("3. Modificar Contratos")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        cant_contratos = int(input("¿Cuántos contratos desea crear? "))
        nuevos_contratos = crear_matriz_contrato(cant_contratos)
        matriz_contratos.extend(nuevos_contratos)
        print("Contratos creados exitosamente.")
    elif opcion == '2':
        mostrar_matriz(encabezados_contratos, matriz_contratos[0:], pos_mil={5}, censurar={1,2})
    elif opcion == '4':
            print("Saliendo al menu principal...")
            menu()
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_contratos()

def gestion_pagos():
    print("----- Gestión de Pagos -----")
    print("1. Crear Pagos")
    print("2. Mostrar Pagos")
    print("3. Modificar Pagos")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        cant_pagos = int(input("¿Cuántos pagos desea crear? "))
        nuevos_pagos = crear_matriz_pagos(cant_pagos)
        matriz_pagos.extend(nuevos_pagos)
        print("Pagos creados exitosamente.")
    elif opcion == '2':
        mostrar_matriz(encabezados_pagos, matriz_pagos[0:],pos_mil={3})
    elif opcion == '3':
        modificar_pago(matriz_pagos[0:])
    elif opcion == '4':
            print("Saliendo al menu principal...")
            menu()
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_pagos()

def gestion_usuarios():
    print("----- Gestión de Usuarios -----")
    print("1. Crear Usuario")
    print("2. Modificar contraseña")
    print("3. Mostrar Usuarios")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        cantidad_usuarios = int(input("¿Cuántos usuarios desea crear? "))
        crear_cant_usuario(cantidad_usuarios)
    elif opcion == '2':
        modificar_usuario()
    elif opcion == '3':
        mostrar_usuarios()
    elif opcion == '4':
            print("Saliendo al menu principal...")
            menu()
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
        print("6. Resumen Estadístico")
        print("7. Salir")
        opcion = input("Seleccione una opción (1-7): ")
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
            mostrar_resumen(matriz_propiedades, matriz_contratos)
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def iniciar_sistema():
    print("----- Bienvenido al sistema -----")
    
    while not iniciar_sesion():
        pass  # sigue pidiendo login hasta que sea correcto

    menu()

# --- EJECUCIÓN ---


if __name__ == "__main__":
    iniciar_sistema()
