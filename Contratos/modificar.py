import json
import os
from FuncAux.validaciones import norm, nonempty, parse_int
from Contratos.busqueda import buscar_contratos, seleccionar_contrato

def cargar_contratos():
    ruta = os.path.join('Contratos', 'datos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_contratos(contratos):
    ruta = os.path.join('Contratos', 'datos.json')
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(contratos, f, indent=2, ensure_ascii=False)

def tipo_estado(opcion):
    """
    Devuelve el estado según la opción seleccionada.
    Lanza ValueError si la opción no es válida.
    """
    if opcion == "0":
        return "Vigente"
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
        # 0) Cargar base
        contratos = cargar_contratos()

        # 1) Buscar contratos (reintentos hasta Enter) — versión neutral, sin filtrar estado
        resultados_ids = buscar_contratos(contratos, norm, parse_int)
        if not resultados_ids:
            print("Búsqueda cancelada.\n")
            return False

        # 2) Seleccionar contrato por ID
        cid = seleccionar_contrato(contratos, resultados_ids, norm)
        if cid is None:
            print("Modificación cancelada.\n")
            return False

        # 3) Robustez por si hay desajuste de tipo en la clave (str/int) sin usar isinstance
        if cid not in contratos:
            cid_alt = str(cid)
            if cid_alt in contratos:
                cid = cid_alt
            else:
                ok = False
                try:
                    cid_alt2 = int(cid)
                    if cid_alt2 in contratos:
                        cid = cid_alt2
                        ok = True
                except Exception:
                    ok = False
                if not ok:
                    raise LookupError("❌ Contrato no encontrado (ID inconsistente).")

        # 4) Tomar referencia y mostrar estado actual
        c = contratos[cid]
        try:
            print(f"Estado actual: {c['Estado']}")
        except (KeyError, AttributeError):
            print("⚠️ Error: el contrato no tiene el campo 'Estado'. Verifique la estructura.\n")
            return False

        continuar = True
        exito = False

        # 5) Pedir nuevo estado con reintentos (solo ValueError reintenta)
        while continuar:
            try:
                op = input("Nuevo estado (0 - Vigente, 1 - Finalizado, 2 - Cancelado, Enter para dejar igual): ").strip()
                nuevo_estado = tipo_estado(op)  # puede lanzar ValueError

                if nuevo_estado == "":
                    print("Se mantiene el estado actual.\n")
                else:
                    c["Estado"] = nuevo_estado
                    guardar_contratos(contratos)
                    print("\n✅ Estado del contrato modificado exitosamente.\n")

                exito = True
                continuar = False  # salir controlado

            except ValueError as e:
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
