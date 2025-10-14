from Contratos.datos import contratos
from FuncAux.validaciones import norm, nonempty, parse_int

def tipo_estado(opcion):
    estado = ""
    if opcion == "0":
        estado = "Activo"
    elif opcion == "1":
        estado = "Finalizado"
    elif opcion == "2":
        estado = "Cancelado"
    else:
        print("Opción no válida, vuelva a intentar.")
    return estado

def modificar_estado_contrato():

    print("----- Modificar Estado del Contrato -----")
    raw_id = input("Ingrese el ID del contrato a modificar: ")
    id_contrato = parse_int(norm(raw_id))
    if id_contrato is None:
        print("ID inválido. Debe ser numérico.\n")
        return False
    
    if id_contrato not in contratos:
        print("❌ Contrato no encontrado.\n")
        return False

    c = contratos[id_contrato]

    # Estado (0/1/2) con Enter para mantener
    print(f"Estado actual: {c['Estado']}")
    op = tipo_estado(input("Nuevo estado (0 - Vigente, 1 - Finalizado, 2 - Cancelado, Enter para dejar igual): ").strip())
    if op in ["Activo", "Finalizado", "Cancelado"]:
        c["Estado"] = op
    elif nonempty(op):
        print("Opción no válida. Se mantiene el estado actual.")
    # Si op está vacío, se mantiene el estado actual

    print("\n✅ Estado del contrato modificado exitosamente.\n")
    return True