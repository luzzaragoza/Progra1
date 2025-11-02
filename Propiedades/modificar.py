import json
import os
from FuncAux.validaciones import norm, nonempty, parse_int
from Propiedades.crear import tipo_propiedad
from Propiedades.busqueda import buscar_propiedades, seleccionar_propiedad

def cargar_propiedades():
    ruta = os.path.join('Propiedades', 'datos.json')
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos.json está mal formateado.")
        return {}

def guardar_propiedades(propiedades):
    ruta = os.path.join('Propiedades', 'datos.json')
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(propiedades, archivo, indent=4, ensure_ascii=False)

def estado_ocupacion(opcion):
    """
    Ocupación de la propiedad dentro de las activas.
    0 -> Libre
    1 -> Ocupada
    "" (Enter) -> mantener
    Lanza ValueError si es inválido.
    """
    if opcion == "0":
        return "Libre"
    elif opcion == "1":
        return "Ocupada"
    elif opcion == "":
        return ""  # mantener
    else:
        raise ValueError("Opción no válida. Ingrese 0, 1 o Enter para mantener.")


def modificar_propiedad():
    """
    Modifica una propiedad usando buscar/seleccionar y muestra resumen de cambios.
    Retorna:
      - True  si hubo cambios y se guardó.
      - False si se canceló o no hubo cambios.
    """
    propiedades = cargar_propiedades()
    print("----- Modificar Propiedad -----")
    try:
        # 1) Buscar con reintentos (neutral)
        resultados_ids = buscar_propiedades(propiedades, norm, parse_int)
        if not resultados_ids:
            print("Búsqueda cancelada.\n")
            return False

        # 2) Seleccionar por ID (devuelve el mismo tipo que tenga el dict)
        pid = seleccionar_propiedad(propiedades, resultados_ids, norm)
        if pid is None:
            print("Modificación cancelada.\n")
            return False

        # 3) Asegurar existencia (tolerar str/int)
        if pid not in propiedades:
            pid_alt = str(pid)
            if pid_alt in propiedades:
                pid = pid_alt
            else:
                ok = False
                try:
                    pid_alt2 = int(pid)
                    if pid_alt2 in propiedades:
                        pid = pid_alt2
                        ok = True
                except Exception:
                    ok = False
                if not ok:
                    raise LookupError("❌ Propiedad no encontrada (ID inconsistente).")

        p = propiedades[pid]

        # 4) Snapshot para el resumen
        try:
            old_dir   = p.get("Direccion", "")
        except (KeyError, AttributeError):
            old_dir = "[Error de lectura]"
        try:
            old_tipo  = p.get("Tipo", "")
        except (KeyError, AttributeError):
            old_tipo = "[Error de lectura]"
        try:
            old_prec  = p.get("PrecioAlquiler", "")
        except (KeyError, AttributeError):
            old_prec = "[Error de lectura]"

        cambios = {}  # {'Campo': (antes, después)}

        # 5) Dirección
        try:
            print(f"\nDirección actual: {p['Direccion']}")
        except (KeyError, AttributeError):
            print("\n[Error en lectura de Dirección actual]")

        nueva_direccion = input("Nueva dirección (Enter para dejar igual): ")
        if nonempty(nueva_direccion):
            try:
                p["Direccion"] = norm(nueva_direccion)
                if p.get("Direccion", "") != old_dir:
                    cambios["Direccion"] = (old_dir, p.get("Direccion", ""))
            except (KeyError, AttributeError):
                print("No se pudo actualizar la Dirección (error de estructura).")

        # 6) Tipo (con reintento por ValueError)
        try:
            print(f"Tipo actual: {p['Tipo']}")
        except (KeyError, AttributeError):
            print("[Error en lectura de Tipo actual]")

        continuar_tipo = True
        while continuar_tipo:
            try:
                opcion_tipo = input("Nuevo tipo (1 - Crear nuevo tipo de propiedad, 2 - Seleccionar tipo ya existente, Enter para dejar igual): ").strip()
                nuevo_tipo = tipo_propiedad(opcion_tipo)  # puede lanzar ValueError
                if nuevo_tipo != "":
                    p["Tipo"] = nuevo_tipo
                    if p.get("Tipo", "") != old_tipo:
                        cambios["Tipo"] = (old_tipo, p.get("Tipo", ""))
                continuar_tipo = False
            except ValueError as e:
                print(f"⚠️ {e}\nIntentá de nuevo.\n")

        # 7) Precio de alquiler (un intento)
        try:
            print(f"Precio actual: ${p['PrecioAlquiler']}")
        except (KeyError, AttributeError):
            print("[Error en lectura de Precio actual]")

        raw_precio = input("Nuevo precio de alquiler (Enter para dejar igual): ").strip()
        if nonempty(raw_precio):
            nuevo_precio = parse_int(norm(raw_precio))
            if nuevo_precio is not None and nuevo_precio > 0:
                try:
                    p["PrecioAlquiler"] = nuevo_precio
                    if p.get("PrecioAlquiler", "") != old_prec:
                        cambios["PrecioAlquiler"] = (old_prec, p.get("PrecioAlquiler", ""))
                except (KeyError, AttributeError):
                    print("No se pudo actualizar el Precio (error de estructura).")
            else:
                print("Ingrese un entero positivo. Se mantiene el precio actual.")

        # 9) Guardado + resumen
        if cambios:
            guardar_propiedades(propiedades)
            print("\nCambios realizados:")
            # orden amable
            orden = ["Direccion", "Tipo", "PrecioAlquiler", "Estado"]
            i = 0
            while i < len(orden):
                k = orden[i]
                if k in cambios:
                    antes, despues = cambios[k]
                    print(f" - {k}: {antes}  →  {despues}")
                i += 1
            print("\n✅ Propiedad modificada exitosamente.\n")
            return True
        else:
            print("\nNo se realizaron cambios en los datos. No se guardaron cambios.\n")
            return False

    except ValueError as e:
        print(f"⚠️ Error de valor: {e}\n")
        return False
    except LookupError as e:
        print(f"{e}\n")
        return False
    except KeyError:
        print("⚠️ Error: falta algún campo en la propiedad (ej. 'Direccion', 'Tipo', 'PrecioAlquiler' o 'Estado').\n")
        return False
    except TypeError:
        print("⚠️ Error de tipo: los datos de la propiedad no son válidos.\n")
        return False
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}\n")
        return False
