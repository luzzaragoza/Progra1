import json
import os

def cargar_propiedades():
    ruta = os.path.join('Propiedades', 'datos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def mostrar_propiedades():
    print("----- Lista de Propiedades -----")
    propiedades = cargar_propiedades()
    
    if not propiedades:  # Si el diccionario está vacío
        print("No hay propiedades registradas.\n")
        return

    for id_propiedad, datos in propiedades.items():
        print(f"ID Propiedad: {id_propiedad}")
        print(f"  Dirección: {datos['Direccion']}")
        print(f"  Tipo: {datos['Tipo']}")
        print(f"  Precio Alquiler (USD): {datos['PrecioAlquiler']}")
        print(f"  Estado: {datos['Estado']}\n")

def mostrar_propiedad(pid, p):
    print(
        f"ID: {pid} | Dirección: {p.get('Direccion','')} | Tipo: {p.get('Tipo','')} | "
        f"Precio: {p.get('PrecioAlquiler','')} | Estado: {p.get('Estado','')}"
    )
