import json
import os

def cargar_inquilinos():
    ruta = os.path.join('Inquilinos', 'datos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def mostrar_inquilinos():
    print("----- Lista de Inquilinos -----")
    inquilinos = cargar_inquilinos()
    
    if not inquilinos:  # Si el diccionario está vacío
        print("No hay inquilinos registrados.\n")
        return

    for id_inquilino, datos in inquilinos.items():
        print(f"ID Inquilino: {id_inquilino}")
        print(f"  Nombre: {datos['Nombre']}")
        print(f"  DNI: {datos['DNI']}")
        print(f"  Email: {datos['Email']}")
        print(f"  Teléfono: {datos['Telefono']}")
        print(f"  Estado: {datos['Estado']}\n")


def mostrar_inquilino(iid, q):
    """Muestra los datos principales del inquilino."""
    print(
        f"ID: {iid} | Nombre: {q.get('Nombre','')} | DNI: {q.get('DNI','')} | "
        f"Email: {q.get('Email','')} | Telefono: {q.get('Telefono','')} | Estado: {q.get('Estado','')}"
    )
