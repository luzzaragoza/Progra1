import json
import os

def cargar_contratos():
    ruta = os.path.join('Contratos', 'datos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def mostrar_contratos():
    contratos = cargar_contratos()
    
    if not contratos:
        print("No hay contratos para mostrar.\n")
        return

    print("----- Lista de Contratos -----")
    for id_contrato, c in contratos.items():
        print(f"ID Contrato: {id_contrato}")
        print(f"  Monto Mensual: ${c['Monto']}")
        print(f"  Fecha Inicio: {c['Fecha_Inicio']}")
        print(f"  Fecha Fin: {c['Fecha_Fin']}")
        print(f"  Estado: {c['Estado']}")
        print("------------------------------")
    print()
