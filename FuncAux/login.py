from Usuarios.crear import usuarios, contraseñas

def validar_usuario(usuario, contraseña):
    if usuario in usuarios:
        indice = usuarios.index(usuario)
        if contraseñas[indice] == contraseña:
            return True
    return False

def iniciar_sesion():
    print("----- Incio de sesión -----")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if validar_usuario(usuario, contraseña):
        print("Login exitoso.\n")
        return True
    else:
        print("Usuario o contraseña incorrectos, vuelva a intentar.\n")
        return False
