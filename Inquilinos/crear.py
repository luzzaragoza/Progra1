from Inquilinos.datos import inquilinos
from FuncAux.validaciones import norm, nonempty, parse_int

def crear_inquilino(id_inquilino):

    nombre = input("Nombre y Apellido: ")
    while not nonempty(nombre):
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre y Apellido: ")
    nombre = norm(nombre)

    while True:
        dni_raw = input("DNI (solo números): ")
        dni = parse_int(dni_raw)
        if dni is None or dni <= 0:
            print("Ingrese un DNI válido por favor.")
            continue
        if any(p["DNI"] == dni for p in inquilinos.values()):
            print("Ese DNI ya está registrado. Ingrese otro.")
            continue
        break

    email = norm(input("Mail: "))
    while not nonempty(email) or ("@" not in email):
        print("Ingrese un email válido por favor.")
        email = norm(input("Mail: "))

    while True:
        tel_raw = input("Teléfono (solo números): ")
        tel = parse_int(tel_raw)
        if tel is not None and tel > 0:
            break
        print("Ingrese un teléfono válido por favor.")

    # Estado por defecto
    estado = "Activo"

    inquilinos[id_inquilino] = {
        "Nombre": nombre,
        "DNI": dni,
        "Email": email,
        "Telefono": tel,
        "Estado": estado,
    }
    print(f"Inquilino con id {id_inquilino} creado exitosamente.\n")
    return id_inquilino


def crear_cant_inquilinos(cant_inquilinos):
    creados = []
    for i in range(cant_inquilinos):
        print(f"--- Ingresando datos del inquilino {i + 1} ---")
        id_inq = len(inquilinos) + 1
        nuevo = crear_inquilino(id_inq)
        creados.append(nuevo)
    print(f"Inquilinos creados exitosamente: ({len(creados)}) \n")
    return creados
