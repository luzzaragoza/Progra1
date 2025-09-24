from Inquilinos.datos import inquilinos

def mostrar_inquilinos():
    print("----- Lista de Inquilinos -----")
    if not inquilinos:  # Si el diccionario está vacío
        print("No hay inquilinos registrados.\n")
        return

    for id_inquilino, datos in inquilinos.items():
        print(f"ID Inquilino: {id_inquilino}")
        print(f"  Nombre: {datos['Nombre']}")
        print(f"  DNI: {datos['DNI']}")
        print(f"  Email: {datos['Email']}")
        print(f"  Teléfono: {datos['Telefono']}")
        print(f"  Estado: {datos['Estado']}\n")