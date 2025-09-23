from Usuarios.datos import usuarios

def mostrar_usuarios():
    print("----- Lista de Usuarios -----")
    if not usuarios:  # Si el diccionario está vacío
        print("No hay usuarios registrados.\n")
        return

    for nombre, datos in usuarios.items():
        print(f"Usuario: {nombre}")
        print(f"  Contrasenia: {datos['Contrasenia']}")
        print(f"  Estado: {datos['Estado']}\n")
