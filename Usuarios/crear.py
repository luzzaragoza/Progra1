import json
import os
from FuncAux.validaciones import norm, nonempty, pwd_ok

def cargar_usuarios():
    ruta = 'Usuarios/datos.json'
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos.json está mal formateado.")
        return {}

def guardar_usuarios(usuarios):
    ruta = 'Usuarios/datos.json'
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

def usuario_existe(usuario):
    usuarios = cargar_usuarios()
    return norm(usuario) in (norm(u) for u in usuarios)

def crear_usuario():
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese nuevo usuario: ").strip()
    while (not nonempty(usuario)) or usuario_existe(usuario):
        if not nonempty(usuario):
            print("El nombre de usuario no puede estar vacío.")
        else:
            print("El usuario ya existe. Intente con otro.")
        usuario = input("Ingrese nuevo usuario: ").strip()

    contrasenia = input("Ingrese contraseña: ").strip()
    while not (nonempty(contrasenia) and pwd_ok(contrasenia)):
        print("La contraseña debe tener al menos 4 caracteres.")
        contrasenia = input("Ingrese contraseña: ").strip()
    
    usuarios[usuario] = {"Contrasenia": contrasenia, "Estado": "activo"}
    guardar_usuarios(usuarios)
    print(f"Usuario '{usuario}' creado exitosamente.\n")
    return usuario

def crear_cant_usuario(cant_usuarios):
    creados = []
    for i in range(cant_usuarios):
        print(f"--- Ingresando datos del usuario {i + 1} ---")
        nuevo = crear_usuario()
        creados.append(nuevo)
    print(f"Usuarios creados exitosamente:({len(creados)}) \n")
    return creados
