from Pagos.datos import pagos
from Pagos.crear import tipo_metodo_pago
from FuncAux.validaciones import parse_int, parse_float, parse_date

def modificar_pago():
    print("\n--- Modificar Pago ---")
    id_pago = parse_int(input("Ingrese el ID del pago a modificar: ").strip())
    
    if id_pago not in pagos:
        print(f"Pago con ID {id_pago} no encontrado.\n")
        return pagos

    print(f"Modificando Pago ID {id_pago}: {pagos[id_pago]}")
    
    id_contrato = parse_int(input("Ingrese nuevo ID Contrato asociado (dejar vacío para no cambiar): ").strip() or pagos[id_pago]["ID Contrato"])
    fecha_pago = parse_date(input("Ingrese nueva Fecha de Pago (YYYY-MM-DD) (dejar vacío para no cambiar): ").strip() or pagos[id_pago]["Fecha"])
    monto = parse_float(input("Ingrese nuevo Monto del Pago (dejar vacío para no cambiar): ").strip() or pagos[id_pago]["Monto"])
    
    print("Seleccione el método de pago:")
    print("0 - Efectivo")
    print("1 - Transferencia")
    print("2 - Tarjeta")
    print("3 - Otro")
    opcion = input("Opción (dejar vacío para no cambiar): ").strip()
    tipo_mpago = tipo_metodo_pago(opcion) if opcion else pagos[id_pago]["Método"]

    pagos[id_pago] = {"ID Contrato": id_contrato, "Fecha": fecha_pago, "Monto": monto, "Método": tipo_mpago}
    print(f"Pago con ID {id_pago} modificado exitosamente.\n")

    return pagos