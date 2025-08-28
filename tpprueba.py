
# Matriz de Inquilinos
matriz_inquilinos = [
    ["ID Inquilino", "Nombre", "DNI", "Email", "Teléfono"],
    [1, "Juan Pérez", "30123456", "juan@mail.com", "+54 11 4567-8901"],
    [2, "María López", "28999888", "maria@mail.com", "+54 9 351 555-1111"],
    [3, "Carlos Díaz", "31222333", "carlos@mail.com", "+54 11 4444-2222"],
    [4, "Ana Torres", "30111222", "ana@mail.com", "+54 341 555-3333"],
    [5, "Luis Gómez", "30333444", "luis@mail.com", "+54 261 444-5555"]
]

# Matriz de Propiedades
matriz_propiedades = [
    ["ID Propiedad", "Dirección", "Tipo", "Precio Alquiler", "Estado"],
    [101, "Av. Siempre Viva 742", "Departamento", 75000, "Libre"],
    [102, "Calle Falsa 123", "Casa", 95000, "Ocupada"],
    [103, "Belgrano 456", "Departamento", 80000, "Libre"],
    [104, "San Martín 321", "Local", 120000, "Ocupada"],
    [105, "Mitre 555", "Casa", 98000, "Libre"]
]

# Matriz de Contratos
matriz_contratos = [
    ["ID Contrato", "ID Propiedad", "ID Inquilino", "Fecha Inicio", "Fecha Fin"],
    [5001, 101, 1, "2025-03-01", "2026-02-28"],
    [5002, 102, 2, "2024-05-15", "2025-05-14"],
    [5003, 103, 3, "2025-01-10", "2026-01-09"],
    [5004, 104, 4, "2025-07-01", "2026-06-30"],
    [5005, 105, 5, "2024-11-20", "2025-11-19"]
]

# Matriz de Pagos
matriz_pagos = [
    ["ID Pago", "ID Contrato", "Fecha Pago", "Monto", "Método"],
    [9001, 5001, "2025-04-01", 75000, "Transferencia"],
    [9002, 5002, "2024-06-01", 95000, "Efectivo"],
    [9003, 5003, "2025-02-01", 80000, "Transferencia"],
    [9004, 5004, "2025-08-01", 120000, "Tarjeta"],
    [9005, 5005, "2024-12-01", 98000, "Transferencia"]
]

#Funciones de CREAR

def crear_inquilino(id_inquilino):
    nombre = input("Nombre completo: ")
    dni = int(input("DNI (solo números): "))
    mail = input("Mail: ")
    telefono = int(input("Teléfono: "))
    estado = "Activo"  # Estado por defecto
    
    return [id_inquilino, nombre, dni, mail, telefono, estado]


def crear_matriz_inquilinos(cant_inquilinos):
    inquilinos = []
    for i in range(cant_inquilinos):
        id_inquilino = len(inquilinos) + 1
        inquilino = crear_inquilino(id_inquilino)
        inquilinos.append(inquilino)
    return inquilinos



def crear_propiedad(id_propiedad):
    direccion = input("Dirección de la propiedad: ")
    tipo = input("Tipo de propiedad (Departamento: [0] / Casa: [2]): ")
    precio_alquiler = int(input("Precio de alquiler (USD): "))
    estado = "Libre"  # Estado por defecto
    
    return [id_propiedad, direccion, tipo, precio_alquiler, estado]


def crear_matriz_propiedades(cant_propiedades):
    propiedades = []
    for i in range(cant_propiedades):
        id_propiedad = len(propiedades) + 1
        propiedad = crear_propiedad(id_propiedad)
        propiedades.append(propiedad)
    return propiedades


def crear_matriz_contrato(cant_contratos):
    contratos=[]
    for i in range(cant_contratos):
        ID_contrato= len(contratos) + 1
        id_propiedad=int(input("ID de la propiedad:"))
        id_inquilino=int(input("ID del inquilino:"))
        fecha_inicio=input("Fecha de inicio (YYYY-MM-DD):")
        fecha_fin=input("Fecha de fin (YYYY-MM-DD):")

        contrato=[id_propiedad, id_inquilino, fecha_inicio, fecha_fin]
        contratos.append(contrato)

    return contratos

def crear_matriz_pagos(cant_pagos):
    pagos=[]
    for i in range(cant_pagos):
        ID_pago= len(pagos) + 1
        id_contrato=int(input("ID del contrato:"))
        fecha_pago=input("Fecha de pago (YYYY-MM-DD):")
        monto=int(input("Monto del pago:"))
        metodo=input("Metodo de pago:")

        pago=[ID_pago, id_contrato, fecha_pago, monto, metodo]
        pagos.append(pago)

    return pagos

#FUNCION DE BUSQUEDA

def busqueda_inquilino(matriz):
    while True:  # Bucle para reintentos
        termino = input("Ingrese nombre o apellido a buscar: ").lower()
        resultados = []

        for i in range(1, len(matriz)):  # asume que la matriz tiene encabezado
            nombre_completo = matriz[i][1].lower()
            if termino in nombre_completo:
                resultados.append(matriz[i])

        if len(resultados) == 0:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i in range(len(resultados)):
                letra = chr(97 + i)
                inquilino = resultados[i]
                print(letra, "-", inquilino[1], "| DNI:", inquilino[2], "| Email:", inquilino[3], "| Tel:", inquilino[4])

            opcion = input("\nSeleccione el inquilino (a, b, c...): ").lower()
            seleccionado = None
            for i in range(len(resultados)):
                letra = chr(97 + i)
                if opcion == letra:
                    inquilino = resultados[i]
                    print("\nHas seleccionado:")
                    print("ID:", inquilino[0], "| Nombre:", inquilino[1], "| DNI:", inquilino[2], "| Email:", inquilino[3], "| Tel:", inquilino[4])
                    seleccionado = inquilino
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")


def busqueda_propiedad(matriz):
    while True:  # Bucle para reintentos
        termino = input("Ingrese dirección o tipo de propiedad a buscar: ").lower()
        resultados = []

        for i in range(len(matriz)):
            direccion_tipo = f"{matriz[i][1]} {matriz[i][2]}".lower()
            if termino in direccion_tipo:
                resultados.append(matriz[i])

        if len(resultados) == 0:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i in range(len(resultados)):
                letra = chr(97 + i) if i < 26 else str(i + 1)
                prop = resultados[i]
                print(f"{letra} - Dirección: {prop[1]} | Tipo: {prop[2]} | Precio: {prop[3]} | Estado: {prop[4]}")

            opcion = input("\nSeleccione la propiedad (letra o número): ").lower()
            seleccionado = None
            for i in range(len(resultados)):
                letra = chr(97 + i) if i < 26 else str(i + 1)
                if opcion == letra:
                    prop = resultados[i]
                    print("\nHas seleccionado:")
                    print(f"ID: {prop[0]} | Dirección: {prop[1]} | Tipo: {prop[2]} | Precio: {prop[3]} | Estado: {prop[4]}")
                    seleccionado = prop
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")


# ---------- FUNCIONES DE MODIFICAR ----------

def modificar_inquilino(matriz):
    id_inquilino = int(input("Ingrese el ID del inquilino a modificar: "))
    for inquilino in matriz:
        if inquilino[0] == id_inquilino:
            nombre = input("Nuevo nombre: ")
            if nombre:
                inquilino[1] = nombre
            dni = input("Nuevo DNI: ")
            if dni:
                inquilino[2] = dni
            mail = input("Nuevo email: ")
            if mail:
                inquilino[3] = mail
            telefono = input("Nuevo teléfono: ")
            if telefono:
                inquilino[4] = telefono
            estado = input("Si desea dar de baja al inquilino ingrese [1] y si desea volver a activarlo [0]:")
            if estado == "1":
                estado = "Inactivo"
            elif estado == "0":
                estado = "Activo"
            else:
                print("Opción no válida. El estado no se modificará.")

            inquilino[5] = estado
            print("Inquilino modificado exitosamente.")
            return
    print("Inquilino no encontrado.")



def modificar_propiedad(matriz):
    id_propiedad = int(input("Ingrese el ID de la propiedad a modificar: "))
    for propiedad in matriz:
        if propiedad[0] == id_propiedad:
            direccion = input("Nueva dirección: ")
            if direccion:
                propiedad[1] = direccion
            tipo = input("Nuevo tipo de propiedad: ")
            if tipo:
                propiedad[2] = tipo
            precio_alquiler = input("Nuevo precio de alquiler: ")
            if precio_alquiler:
                propiedad[3] = int(precio_alquiler)
            estado = input("Si desea dar de baja la propiedad ingrese [1] y si desea volver a activarla [0]:")
            if estado == "1":
                estado = "Ocupada"
            elif estado == "0":
                estado = "Libre"
            else:
                print("Opción no válida. El estado no se modificará.")

            propiedad[4] = estado
            print("Propiedad modificada exitosamente.")
            return
    print("Propiedad no encontrada.")



def modificar_contrato(matriz):
    id_contrato = int(input("Ingrese el ID del contrato a modificar: "))
    for contrato in matriz:
        if contrato[0] == id_contrato:
            id_propiedad = input("Nuevo ID de propiedad: ")
            if id_propiedad:
                contrato[1] = int(id_propiedad)
            id_inquilino = input("Nuevo ID de inquilino: ")
            if id_inquilino:
                contrato[2] = int(id_inquilino)
            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
            if fecha_inicio:
                contrato[3] = fecha_inicio
            fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
            if fecha_fin:
                contrato[4] = fecha_fin

            print("Contrato modificado exitosamente.")
            return
    print("Contrato no encontrado.")



def modificar_pago(matriz):
    id_pago = int(input("Ingrese el ID del pago a modificar: "))
    for pago in matriz:
        if pago[0] == id_pago:
            id_contrato = input("Nuevo ID de contrato: ")
            if id_contrato:
                pago[1] = int(id_contrato)
            fecha_pago = input("Nueva fecha de pago (YYYY-MM-DD): ")
            if fecha_pago:
                pago[2] = fecha_pago
            monto = input("Nuevo monto: ")
            if monto:
                pago[3] = int(monto)
            metodo = input("Nuevo método de pago: ")
            if metodo:
                pago[4] = metodo

            print("Pago modificado exitosamente.")
            return
    print("Pago no encontrado.")


#Funciones Aux

def mostrar_matriz(encabezados, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for titulo in encabezados: # Imprimir encabezados
        print(titulo, end="\t")
    print()
    for fila in range(filas):
        for columna in range(columnas):
            print(matriz[fila][columna], end="\t")
        print()


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


#Programa principal

def menu():
    while True:
        print("----- Menú de Gestión de Alquileres -----")
        print("1. Gestión de Inquilinos")
        print("2. Gestión de Propiedades")
        print("3. Gestión de Contratos")
        print("4. Gestión de Pagos")
        print("5. Salir")
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
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()