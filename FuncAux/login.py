from Usuarios.datos import usuarios

def validar_usuario(usuario, contrasenia):
    """Verifica si el usuario existe y la contraseña coincide."""
    if usuario in usuarios:
        return usuarios[usuario]["Contrasenia"] == contrasenia
    return False

def iniciar_sesion():
    print("----- Inicio de sesión -----")
    usuario = input("Usuario: ").strip()
    contrasenia = input("Contrasenia: ").strip()

    if validar_usuario(usuario, contrasenia):
        print("Login exitoso.\n")
        return True
    else:
        print("Usuario o contraseña incorrectos, vuelva a intentar.\n")
        return False
