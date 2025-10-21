from Contratos.datos import contratos
from FuncAux.validaciones import norm, nonempty, parse_int

def tipo_estado(opcion):
    """
    Devuelve el estado según la opción seleccionada.
    Lanza ValueError si la opción no es válida.
    """
    if opcion == "0":
        return "Activo"
    elif opcion == "1":
        return "Finalizado"
    elif opcion == "2":
        return "Cancelado"
    elif opcion == "":
        # Enter = mantener estado actual
        return ""
    else:
        raise ValueError("Opción no válida. Ingrese 0, 1, 2 o Enter para mantener.")


def modificar_estado_contrato():
    print("----- Modificar Estado del Contrato -----")
    try:
        raw_id = input("Ingrese el ID del contrato a modificar: ")
        id_contrato = parse_int(norm(raw_id))
        if id_contrato is None:
            raise ValueError("ID inválido. Debe ser numérico.")

        if id_contrato not in contratos:
            raise LookupError("❌ Contrato no encontrado.")

        c = contratos[id_contrato]
        print(f"Estado actual: {c['Estado']}")

        continuar = True
        exito = False

        while continuar:
            try:
                op = input("Nuevo estado (0 - Activo, 1 - Finalizado, 2 - Cancelado, Enter para dejar igual): ").strip()
                nuevo_estado = tipo_estado(op)  # puede lanzar ValueError

                if nuevo_estado == "":
                    print("Se mantiene el estado actual.\n")
                else:
                    c["Estado"] = nuevo_estado
                    print("\n✅ Estado del contrato modificado exitosamente.\n")

                exito = True
                continuar = False  # sale del while de forma controlada

            except ValueError as e:
                # Solo esta excepción permite reintentar
                print(f"⚠️ {e}")
                print("Intentá de nuevo.\n")

        return exito

    except ValueError as e:
        print(f"⚠️ Error de valor: {e}\n")
        return False
    except LookupError as e:
        print(f"{e}\n")
        return False
    except KeyError:
        print("⚠️ Error: el contrato no tiene el campo 'Estado'. Verifique la estructura.\n")
        return False
    except TypeError:
        print("⚠️ Error de tipo: los datos del contrato no son válidos.\n")
        return False
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}\n")
        return False
