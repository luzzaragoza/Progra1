from Pagos.datos import pagos
from FuncAux.validaciones import parse_int, nonempty, norm, parse_date, parse_float  # <- lambdas/funcs de validación

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
    print(f"Pago con ID {id_pago} creado exitosamente.\n")

    return pagos

def crear_cant_pagos(cant_pagos):
    creados = []
    for i in range(cant_pagos):
        print(f"--- Ingresando datos del pago {i + 1} ---")
        id_pago = len(pagos) + 1
        nuevo = crear_pagos(id_pago)
        creados.append(nuevo)
    print(f"Pagos creados exitosamente: ({len(creados)}) \n")
    return creados