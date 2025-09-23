from Usuarios.datos import usuarios

def usuario_existe(usuario):
    """Devuelve True si el usuario ya está en el diccionario."""
    return usuario in usuarios

def crear_usuario():
    usuario = input("Ingrese nuevo usuario: ").strip()
    while usuario_existe(usuario):
        print("El usuario ya existe. Intente con otro.")
        usuario = input("Ingrese nuevo usuario: ").strip()
    contrasenia = input("Ingrese contraseña: ").strip()
    usuarios[usuario] = {"Contrasenia": contrasenia, "Estado": "Activo"}
    print(f"Usuario '{usuario}' creado exitosamente.\n")
    return usuario

def crear_cant_usuario(cant_usuarios):
    creados = []
    for i in range(cant_usuarios):
        print(f"--- Ingresando datos del usuario {i + 1} ---")
        nuevo = crear_usuario()
        creados.append(nuevo)
    print("Usuarios creados:", creados)