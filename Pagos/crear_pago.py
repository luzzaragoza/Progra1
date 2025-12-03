import json
import os
from FuncAux.validaciones import parse_int, nonempty, norm, parse_date, parse_float
from Pagos.tipos_pagos import tipo_pago
from Contratos.busqueda_contrato import buscar_contratos, seleccionar_contrato
from Contratos.modificar_contrato import cargar_contratos


def cargar_pagos():
    ruta = 'Pagos/datos_pago.json'  
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos_pagos.json está mal formateado.")  
        return {}


def guardar_pagos(pagos):
    ruta = 'Pagos/datos_pagos.json' 
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(pagos, archivo, indent=4, ensure_ascii=False)


def crear_pagos(id_pago):
    pagos = cargar_pagos()
    
    print(f"\n--- Creando Pago ID {id_pago} ---")
    # Seleccionar contrato asociado
    contratos = cargar_contratos()
    resultados_ids = buscar_contratos(contratos, norm, parse_int)
    if not resultados_ids:
        print("No se encontraron contratos. Cancelando creación de pago.\n")
        return None
    id_contrato = seleccionar_contrato(contratos, resultados_ids, norm)
    if id_contrato is None:
        print("Selección de contrato cancelada. Cancelando creación de pago.\n")
        return None


    fecha_pago = parse_date(input("Ingrese Fecha de Pago (AAAA-MM-DD): ").strip())
    monto = parse_float(input("Ingrese Monto del Pago: ").strip())
    
    print("Seleccione:")
    print("1 - Crear tipo de pago nuevo")
    print("1 - Seleccionar tipo de pago existente")
    opcion = input("Opción: ").strip()
    tipo_mpago = tipo_pago(opcion)

    pagos[id_pago] = {"ID Contrato": id_contrato, "Fecha": fecha_pago, "Monto": monto, "Método": tipo_mpago}
    guardar_pagos(pagos)
    print(f"Pago con ID {id_pago} creado exitosamente.\n")

    return pagos


def crear_cant_pagos(cant_pagos):
    creados = []
    for i in range(cant_pagos):
        print(f"--- Ingresando datos del pago {i + 1} ---")
        pagos = cargar_pagos()
        id_pago = int(max((pagos.keys()))) + 1
        nuevo = crear_pagos(id_pago)
        creados.append(nuevo)
    print(f"Pagos creados exitosamente: ({len(creados)}) \n")
    return creados
