# Propiedades/baja.py
import json
import os
from FuncAux.validaciones import parse_int, norm
from Propiedades.mostrar import mostrar_propiedad

def cargar_propiedades():
    ruta = 'Propiedades/datos.json'
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos.json está mal formateado.")
        return {}

def guardar_propiedades(propiedades):
    ruta = 'Propiedades/datos.json'
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(propiedades, archivo, indent=4, ensure_ascii=False)

def baja_propiedad():
    """
    Baja lógica: Estado -> 'Inactiva'.
    Si ya está Inactiva, informa y termina.
    """
    propiedades = cargar_propiedades()
    
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

        else:
            pid_str = str(pid)
            if pid_str not in propiedades:
                print(f"No existe la propiedad con ID {pid}.\n")
            else:
                p = propiedades[pid_str]
                print("\nSeleccionada:")
                mostrar_propiedad(pid_str, p)

                if str(p.get("Estado","")).lower() == "inactiva":
                    print("La propiedad ya está Inactiva.\n")
                    continuar = False
                else:
                    conf = norm(input("Confirmar baja lógica (s/n): "))
                    if conf in ("s", "si", "sí"):
                        p["Estado"] = "Inactiva"
                        guardar_propiedades(propiedades)
                        print("Baja realizada. (Estado = Inactiva)\n")
                        exito = True
                        continuar = False
                    else:
                        print("Baja cancelada.\n")
                        continuar = False

    return exito
