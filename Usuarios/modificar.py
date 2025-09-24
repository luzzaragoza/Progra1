from Usuarios.datos import usuarios
from FuncAux.validaciones import norm, nonempty, pwd_ok

def cambiar_contrasenia():
    print("----- Modificar Usuario -----")
    usuario_ing = input("Ingrese el usuario a modificar contraseña: ")

    # Busco la clave real de forma case-insensitive usando 'norm'
    clave_real = next((k for k in usuarios if norm(k) == norm(usuario_ing)), None)
    if not clave_real:
        print("El usuario no existe.\n")
        return False

    nueva = input("Ingrese la nueva contraseña: ").strip()
    while not (nonempty(nueva) and pwd_ok(nueva)):
        print("La contraseña debe tener al menos 4 caracteres.")
        nueva = input("Ingrese la nueva contraseña: ").strip()

    usuarios[clave_real]["Contrasenia"] = nueva  # no lower; respetamos lo que escribe
    print("Contraseña modificada exitosamente.\n")
    return True