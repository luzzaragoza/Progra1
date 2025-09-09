def login():
    usuario_correcto = "admin"
    contrasenia_correcta = "1234"

    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contrasenia = input("Contraseña: ")

        if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
            print("Login exitoso.\n")
            return True
        else:
            intentos -= 1
            print("Usuario o contraseña incorrectos. Intentos restantes:", intentos)

    print("Acceso denegado.")
    return False