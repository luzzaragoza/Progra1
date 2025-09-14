def crear_inquilino(id_inquilino):
    nombre = input("Nombre completo: ")
    dni = int(input("DNI (solo números): "))
    mail = input("Mail: ")
    telefono = int(input("Teléfono: "))
    estado = "Activo" 
    
    return [id_inquilino, nombre, dni, mail, telefono, estado]


def crear_matriz_inquilinos(cant_inquilinos):
    inquilinos = []
    for i in range(cant_inquilinos):
        id_inquilino = len(inquilinos) + 1
        inquilino = crear_inquilino(id_inquilino)
        inquilinos.append(inquilino)
    return inquilinos

