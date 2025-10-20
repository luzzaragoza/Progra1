# Propiedades/baja.py
from Propiedades.datos import propiedades
from FuncAux.validaciones import parse_int, norm
from Propiedades.mostrar import mostrar_propiedad

def baja_propiedad():
    """
    Baja lógica: Estado -> 'Inactiva'.
    Si ya está Inactiva, informa y termina.
    """
    continuar = True
    exito = False

    while continuar:
        entrada = input("ID de la propiedad a dar de baja (0 para cancelar): ").strip()
        pid = parse_int(entrada)

        if pid is None:
            print("ID inválido. Probá nuevamente.\n")

        elif pid == 0:
            print("Operación cancelada.")
            continuar = False

        elif pid not in propiedades:
            print(f"No existe la propiedad con ID {pid}.\n")

        else:
            p = propiedades[pid]
            print("\nSeleccionada:")
            mostrar_propiedad(pid, p)

            if str(p.get("Estado","")).lower() == "inactiva":
                print("La propiedad ya está Inactiva.\n")
                continuar = False
            else:
                conf = norm(input("Confirmar baja lógica (s/n): "))
                if conf in ("s", "si", "sí"):
                    p["Estado"] = "Inactiva"
                    print("Baja realizada. (Estado = Inactiva)\n")
                    exito = True
                    continuar = False
                else:
                    print("Baja cancelada.\n")
                    continuar = False

    return exito
