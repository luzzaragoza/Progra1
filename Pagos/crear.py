import json
import os
from FuncAux.validaciones import parse_int, nonempty, norm, parse_date, parse_float

def cargar_pagos():
    ruta = os.path.join('Pagos', 'datos.json')
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos.json está mal formateado.")
        return {}

def guardar_pagos(pagos):
    ruta = os.path.join('Pagos', 'datos.json')
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(pagos, archivo, indent=4, ensure_ascii=False)

def tipo_metodo_pago(opcion):
    tipo = ""
    if opcion == "0":
        tipo = "Efectivo"
    elif opcion == "1":
        tipo = "Transferencia"
    elif opcion == "2":
        tipo = "Tarjeta"
    elif opcion == "3":
        tipo = input("Ingrese el método de pago: ").strip()
    else:
        print("Opción no válida, vuelva a intentar.")
    return tipo


def crear_pagos(id_pago):
    pagos = cargar_pagos()
    
    print(f"\n--- Creando Pago ID {id_pago} ---")
    id_contrato = parse_int(input("Ingrese ID Contrato asociado: ").strip())
    fecha_pago = parse_date(input("Ingrese Fecha de Pago (YYYY-MM-DD): ").strip())
    monto = parse_float(input("Ingrese Monto del Pago: ").strip())
    
    print("Seleccione el método de pago:")
    print("0 - Efectivo")
    print("1 - Transferencia")
    print("2 - Tarjeta")
    print("3 - Otro")
    opcion = input("Opción: ").strip()
    tipo_mpago = tipo_metodo_pago(opcion)

    pagos[id_pago] = {"ID Contrato": id_contrato, "Fecha": fecha_pago, "Monto": monto, "Método": tipo_mpago}
    guardar_pagos(pagos)
    print(f"Pago con ID {id_pago} creado exitosamente.\n")

    return pagos

def crear_cant_pagos(cant_pagos):
    creados = []
    for i in range(cant_pagos):
        print(f"--- Ingresando datos del pago {i + 1} ---")
        pagos = cargar_pagos()
        id_pago = len(pagos) + 1
        nuevo = crear_pagos(id_pago)
        creados.append(nuevo)
    print(f"Pagos creados exitosamente: ({len(creados)}) \n")
    return creados
