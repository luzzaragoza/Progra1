usuarios = ["admin"]
contraseñas = ["1234"]
estado_usuarios = ["activo"]

def usuario_existe(user, matriz):
    if user in matriz:
        return True
    return False

def crear_usuario():
    usuario = input("Ingrese nuevo usuario: ")
    while usuario_existe(usuario, usuarios):
        print("El usuario ya existe. Intente con otro.")
        usuario = input("Ingrese nuevo usuario: ")
    contraseña = input("Ingrese nueva contraseña: ")
    estado = "Activo"

    estado_usuarios.append(estado)
    usuarios.append(usuario)
    contraseñas.append(contraseña)
    print("Usuario creado exitosamente.\n")

def crear_matriz_usuario(cant_usuarios):
    matriz = []
    for i in range(cant_usuarios):
        print(f"--- Ingresando datos del usuario {i + 1} ---")
        usuario = input("Ingrese nombre de usuario: ")
        while usuario_existe(usuario, usuarios):
            print("El usuario ya existe. Intente con otro.")
            usuario = input("Ingrese nombre de usuario: ")
        
        contraseña = input("Ingrese contraseña: ")

        usuarios.append(usuario)
        contraseñas.append(contraseña)
        matriz.append([usuario, contraseña])
    return matriz