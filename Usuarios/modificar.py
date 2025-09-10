from Usuarios.crear import usuarios, contraseñas, estado_usuarios

def modificar_usuario():
    print("----- Modificar Usuario -----")
    usuario = input("Ingrese el usuario a modificar: ")
    if usuario in usuarios:
        indice = usuarios.index(usuario)
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        contraseñas[indice] = nueva_contraseña
        print("Contraseña modificada exitosamente.\n")
        estado = input("Si desea dar de baja el usuario ingrese [1] y si desea volver a activarlo [0]: ")
        if estado == "1":
            estado_usuarios[indice] = "inactivo"
        elif estado == "0":
            estado_usuarios[indice] = "activo"
    else:
        print("El usuario no existe.\n")