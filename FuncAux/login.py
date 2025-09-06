def login():
    usuario_correcto = "admin"
    contraseña_correcta = "1234"

    intentos = 3
    while intentos > 0:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        if usuario == usuario_correcto and contraseña == contraseña_correcta:
            print("Login exitoso.\n")
            return True
        else:
            intentos -= 1
            print("Usuario o contraseña incorrectos. Intentos restantes:", intentos)

    print("Acceso denegado.")
    return False