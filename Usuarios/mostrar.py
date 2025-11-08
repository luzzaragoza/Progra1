import json
import os

def cargar_usuarios():
    ruta = 'Usuarios/datos.json'
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def mostrar_usuarios():
    print("----- Lista de Usuarios -----")
    usuarios = cargar_usuarios()
    
    if not usuarios:  # Si el diccionario está vacío
        print("No hay usuarios registrados.\n")
        return

    for nombre, datos in usuarios.items():
        print(f"Usuario: {nombre}")
        print(f"  Contrasenia: {datos['Contrasenia']}")
        print(f"  Estado: {datos['Estado']}\n")
