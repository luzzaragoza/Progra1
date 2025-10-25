import json
import os
from FuncAux.validaciones import norm, nonempty, parse_int
from Propiedades.crear import tipo_propiedad

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
    propiedades = cargar_propiedades()
    
    print("----- Modificar Propiedad -----")
    try:
        raw_id = input("Ingrese el ID de la propiedad a modificar: ")
        id_prop = parse_int(norm(raw_id))
        if id_prop is None:
            raise ValueError("ID inválido. Debe ser numérico.")

        id_prop_str = str(id_prop)
        if id_prop_str not in propiedades:
            raise LookupError("❌ Propiedad no encontrada.")

        p = propiedades[id_prop_str]

        # Dirección
        print(f"\nDirección actual: {p['Direccion']}")
        nueva_direccion = input("Nueva dirección (Enter para dejar igual): ")
        if nonempty(nueva_direccion):
            p["Direccion"] = norm(nueva_direccion)

        # Tipo (0/1/2 o Enter) con reintento por ValueError
        print(f"Tipo actual: {p['Tipo']}")
        continuar_tipo = True
        while continuar_tipo:
            try:
                opcion_tipo = input("Nuevo tipo (0 - Casa, 1 - Departamento, 2 - Otro, Enter para dejar igual): ").strip()
                nuevo_tipo = tipo_propiedad(opcion_tipo)  # usa tu función separada
                if nuevo_tipo != "":
                    p["Tipo"] = nuevo_tipo
                continuar_tipo = False
            except ValueError as e:
                print(f"⚠️ {e}\nIntentá de nuevo.\n")

        # Precio de alquiler (un intento; si es inválido, mantiene)
        print(f"Precio actual: ${p['PrecioAlquiler']}")
        raw_precio = input("Nuevo precio de alquiler (Enter para dejar igual): ").strip()
        if nonempty(raw_precio):
            nuevo_precio = parse_int(norm(raw_precio))
            if nuevo_precio is not None and nuevo_precio > 0:
                p["PrecioAlquiler"] = nuevo_precio
            else:
                print("Ingrese un entero positivo. Se mantiene el precio actual.")

        # Estado de ocupación (solo si NO está Inactiva)
        print(f"Estado actual: {p['Estado']}")
        if str(p.get("Estado","")).lower() == "inactiva":
            print("La propiedad está Inactiva. Para activarla usá alta_propiedad().")
        else:
            continuar_estado = True
            while continuar_estado:
                try:
                    op_est = input("Nuevo estado (0 - Libre, 1 - Ocupada, Enter para mantener): ").strip()
                    nuevo_est = estado_ocupacion(op_est)  # validador de ocupación
                    if nuevo_est != "":
                        p["Estado"] = nuevo_est
                    continuar_estado = False
                except ValueError as e:
                    print(f"⚠️ {e}\nIntentá de nuevo.\n")

        guardar_propiedades(propiedades)
        print("\n✅ Propiedad modificada exitosamente.\n")
        return True

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
