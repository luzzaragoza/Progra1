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


'''def generar_id(lista):
    """Devuelve el siguiente ID basado en la última fila de la lista.
    Suponemos que cada elemento tiene el ID en la posición 0."""
    return (lista[-1][0] + 1) if lista else 1


def crear_inquilino(id_inquilino):
    nombre = input("Nombre completo: ")
    dni = int(input("DNI (solo números): "))
    mail = input("Mail: ")
    telefono = int(input("Teléfono: "))
    estado = "Activo"  # Estado por defecto
    return [id_inquilino, nombre, dni, mail, telefono, estado]


def crear_matriz_inquilinos(cant_inquilinos, inquilinos=None):
    """Crea 'cant_inquilinos' y los agrega a la lista 'inquilinos' si se proporciona.
    Si inquilinos es None, crea una nueva lista."""
    if inquilinos is None:
        inquilinos = []
    for _ in range(cant_inquilinos):
        id_inquilino = generar_id(inquilinos)
        inquilino = crear_inquilino(id_inquilino)
        inquilinos.append(inquilino)
    return inquilinos


def agregar_inquilino(inquilinos):
    """Agrega un único inquilino a la lista existente."""
    id_inquilino = generar_id(inquilinos)
    inquilino = crear_inquilino(id_inquilino)
    inquilinos.append(inquilino)


def imprimir_inquilinos(inquilinos):
    print("{:<4} {:<25} {:<10} {:<25} {:<12} {:<8}".format("ID","NOMBRE","DNI","MAIL","TEL","ESTADO"))
    for i in inquilinos:
        print("{:<4} {:<25} {:<10} {:<25} {:<12} {:<8}".format(i[0], i[1], i[2], i[3], i[4], i[5]))'''