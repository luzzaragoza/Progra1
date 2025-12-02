import json
import os
from FuncAux.validaciones import norm, nonempty, pwd_ok

def cargar_usuarios():
    ruta = 'Usuarios/datos_usuarios.json'  
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos_usuarios.json está mal formateado.")  
        return {}

def guardar_usuarios(usuarios):
    ruta = 'Usuarios/datos_usuarios.json'  
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4, ensure_ascii=False)

def cambiar_contrasenia():
    usuarios = cargar_usuarios()
    
    print("----- Modificar Usuario -----")
    usuario_ing = input("Ingrese el usuario a modificar contraseña: ")

    clave_real = next((k for k in usuarios if norm(k) == norm(usuario_ing)), None)
    if not clave_real:
        print("El usuario no existe.\n")
        return False

    nueva = input("Ingrese la nueva contraseña: ").strip()
    while not (nonempty(nueva) and pwd_ok(nueva)):
        print("La contraseña debe tener al menos 4 caracteres.")
        nueva = input("Ingrese la nueva contraseña: ").strip()

    usuarios[clave_real]["Contrasenia"] = nueva
    guardar_usuarios(usuarios)
    print("Contraseña modificada exitosamente.\n")
    return True
