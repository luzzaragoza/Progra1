from Usuarios.datos import usuarios

def cambiar_contrasenia():
    print("----- Modificar Usuario -----")
    usuario = input("Ingrese el usuario a modificar contraseña: ").strip()

    if usuario in usuarios:
        nueva_contrasenia = input("Ingrese la nueva contraseña: ").strip()
        usuarios[usuario]["Contrasenia"] = nueva_contrasenia
        print("Contraseña modificada exitosamente.")
    else:
        print("El usuario no existe.\n")
