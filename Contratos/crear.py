import json
import os
from FuncAux.validaciones import norm, nonempty, parse_int, parse_float, parse_date
from Inquilinos.busqueda import buscar_inquilinos, seleccionar_inquilino
from Inquilinos.crear import cargar_inquilinos
from Propiedades.busqueda import buscar_propiedades, seleccionar_propiedad
from Propiedades.crear import cargar_propiedades

# Cargar contratos desde JSON
def cargar_contratos():
    ruta = 'Contratos/datos.json'
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # Si no existe, crear uno vacío
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=2, ensure_ascii=False)
        return {}

# Guardar contratos en JSON
def guardar_contratos(contratos):
    ruta = 'Contratos/datos.json'
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(contratos, f, indent=2, ensure_ascii=False)

# Crear un contrato
def crear_contrato(contratos, id_contrato):
    # ID de inquilino
# ID de inquilino (busco y selecciono, no escribo ID a mano)
    while True:
        # 1) cargar diccionario actual de inquilinos (ajusta a tu función real)
        inquilinos = cargar_inquilinos()  # si tu función se llama distinto, cambiala acá

        # 2) buscar por texto o por ID exacto
        resultados = buscar_inquilinos(inquilinos, norm, parse_int)
        if not resultados:
            print("Búsqueda cancelada o sin resultados.\n")
            continue  # o return None si querés abortar crear_contrato

        # 3) mostrar resultados y dejar elegir
        elegido = seleccionar_inquilino(inquilinos, resultados, norm)
        if elegido is None:
            print("Selección cancelada.\n")
            continue  # o return None

        # 4) normalizo el tipo (puede volver str o int según JSON)
        id_inq = parse_int(str(elegido))
        if id_inq is not None and id_inq > 0:
            break
        print("El ID elegido no es válido, reintentá.\n")


    # ID de propiedad
# ID de propiedad (busco y selecciono)
    while True:
        propiedades = cargar_propiedades()
        resultados = buscar_propiedades(propiedades, norm, parse_int)
        if not resultados:
            print("Búsqueda cancelada o sin resultados.\n")
            continue  # o return None

        elegido = seleccionar_propiedad(propiedades, resultados, norm)
        if elegido is None:
            print("Selección cancelada.\n")
            continue  # o return None

        id_prop = parse_int(str(elegido))
        if id_prop is not None and id_prop > 0:
            break
        print("El ID elegido no es válido, reintentá.\n")


    # Monto mensual
    while True:
        raw_monto = input("Monto mensual (en USD): ")
        monto = parse_int(raw_monto)
        if monto is not None and monto > 0:
            break
        print("Ingrese un monto válido por favor.")

    # Fecha de inicio
    while True:
        raw_fecha_inicio = input("Fecha de inicio (AAAA-MM-DD): ")
        fecha_inicio = parse_date(raw_fecha_inicio)
        if fecha_inicio is not None:
            break
        print("Ingrese una fecha válida por favor.")

    # Fecha de fin
    while True:
        raw_fecha_fin = input("Fecha de fin (AAAA-MM-DD): ")
        fecha_fin = parse_date(raw_fecha_fin)
        if fecha_fin is not None:
            break
        print("Ingrese una fecha válida por favor.")

    # Estado
    estado = "Activo"

    # Crear el contrato
    contrato = {
        "ID_Inquilino": id_inq,
        "ID_Propiedad": id_prop,
        "Monto": monto,
        "Fecha_Inicio": fecha_inicio,
        "Fecha_Fin": fecha_fin,
        "Estado": estado,
    }

    contratos[str(id_contrato)] = contrato  # <-- clave como string para JSON

    print(f"Contrato con id {id_contrato} creado exitosamente.\n")
    return contrato


# Crear varios contratos
def crear_cant_contratos(cant_contratos):
    contratos = cargar_contratos()
    creados = []
    for i in range(cant_contratos):
        print(f"--- Ingresando datos del contrato {i + 1} ---")
        id_con = int(max((contratos.keys()))) + 1 if contratos else 1
        nuevo = crear_contrato(contratos, id_con)
        creados.append(nuevo)
    guardar_contratos(contratos)
    print(f"Contratos creados exitosamente: ({len(creados)}) \n")
    return creados
