# Inquilinos/baja.py
import json
import os
from FuncAux.validaciones import parse_int, norm
from Inquilinos.mostrar import mostrar_inquilino

def cargar_inquilinos():
    ruta = os.path.join('Inquilinos', 'datos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_inquilinos(inquilinos):
    ruta = os.path.join('Inquilinos', 'datos.json')
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(inquilinos, f, indent=2, ensure_ascii=False)

def baja_inquilino():
    """
    Baja lógica del inquilino: cambia Estado -> 'Inactivo'.
    Usa un while con condición de control clara, sin breaks incondicionales.
    Retorna True si se hizo la baja, False si no.
    """
    continuar = True
    exito = False  # para saber si se concretó la baja

    while continuar:
        entrada = input("Ingrese el ID del inquilino a dar de baja (0 para cancelar): ").strip()
        iid = parse_int(entrada)

        inquilinos = cargar_inquilinos()
        
        # condición de salida: cancelar o ID inválido
        if iid is None:
            print("ID inválido. Intente nuevamente.\n")
        elif iid == 0:
            print("Operación cancelada.")
            continuar = False  # sale del while sin break
        elif iid not in inquilinos:
            print(f"No se encontró un inquilino con ID {iid}.\n")
        else:
            q = inquilinos[iid]
            print("\nSeleccionado:")
            mostrar_inquilino(iid, q)

            if str(q.get("Estado","")).lower() == "inactivo":
                print("El inquilino ya está Inactivo.\n")
                continuar = False
            else:
                confirma = norm(input("¿Confirmar baja lógica? (s/n): "))
                if confirma in ("s", "si", "sí"):
                    q["Estado"] = "Inactivo"
                    guardar_inquilinos(inquilinos)
                    print("Baja realizada correctamente.\n")
                    exito = True
                    continuar = False
                else:
                    print("Baja cancelada.\n")
                    continuar = False

    return exito
