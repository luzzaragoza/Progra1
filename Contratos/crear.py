import json
import os
from FuncAux.validaciones import norm, nonempty, parse_int, parse_float, parse_date

# Cargar contratos desde JSON
def cargar_contratos():
    ruta = os.path.join('Contratos', 'datos.json')
    if not os.path.exists(ruta):  # Si no existe, crear uno vacío
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=2, ensure_ascii=False)
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

# Guardar contratos en JSON
def guardar_contratos(contratos):
    ruta = os.path.join('Contratos', 'datos.json')
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(contratos, f, indent=2, ensure_ascii=False)

# Crear un contrato
def crear_contrato(contratos, id_contrato):
    # ID de inquilino
    while True:
        raw_id_inq = input("ID de inquilino: ")
        id_inq = parse_int(raw_id_inq)
        if id_inq is not None and id_inq > 0:
            break
        print("Ingrese un ID válido por favor.")

    # ID de propiedad
    while True:
        raw_id_prop = input("ID de propiedad: ")
        id_prop = parse_int(raw_id_prop)
        if id_prop is not None and id_prop > 0:
            break
        print("Ingrese un ID válido por favor.")

    # Monto mensual
    while True:
        raw_monto = input("Monto mensual (en USD): ")
        monto = parse_int(raw_monto)
        if monto is not None and monto > 0:
            break
        print("Ingrese un monto válido por favor.")

    # Fecha de inicio
    while True:
        raw_fecha_inicio = input("Fecha de inicio (DD-MM-AAAA): ")
        fecha_inicio = parse_date(raw_fecha_inicio)
        if fecha_inicio is not None:
            break
        print("Ingrese una fecha válida por favor.")

    # Fecha de fin
    while True:
        raw_fecha_fin = input("Fecha de fin (DD-MM-AAAA): ")
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
        id_con = len(contratos) + 1
        nuevo = crear_contrato(contratos, id_con)
        creados.append(nuevo)
    guardar_contratos(contratos)
    print(f"Contratos creados exitosamente: ({len(creados)}) \n")
    return creados
