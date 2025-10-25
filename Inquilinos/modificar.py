import json
import os
from FuncAux.validaciones import norm, nonempty, parse_int

def cargar_inquilinos():
    ruta = os.path.join('Inquilinos', 'datos.json')
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_inquilinos(inquilinos):
    ruta = os.path.join('Inquilinos', 'datos.json')
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(inquilinos, f, indent=2, ensure_ascii=False)

def modificar_inquilino():
    print("----- Modificar Inquilino -----")
    raw_id = input("Ingrese el ID del inquilino a modificar: ")
    id_inq = parse_int(norm(raw_id))
    if id_inq is None:
        print("ID inválido. Debe ser numérico.\n")
        return False

    inquilinos = cargar_inquilinos()
    
    if id_inq not in inquilinos:
        print("❌ Inquilino no encontrado.\n")
        return False

    i = inquilinos[id_inq]

    # Nombre
    print(f"\nNombre actual: {i['Nombre']}")
    nuevo_nombre = input("Nuevo nombre (Enter para dejar igual): ")
    if nonempty(nuevo_nombre):
        i["Nombre"] = norm(nuevo_nombre)

    # DNI
    print(f"DNI actual: {i['DNI']}")
    raw_dni = input("Nuevo DNI (solo números / Enter para dejar igual): ")
    raw_dni = norm(raw_dni)
    if nonempty(raw_dni):
        nuevo_dni = parse_int(raw_dni)
        if nuevo_dni is not None and nuevo_dni > 0:
            if any(inq["DNI"] == nuevo_dni and inq_id != id_inq for inq_id, inq in inquilinos.items()):
                print("Ese DNI ya está registrado a otro inquilino. Se mantiene el DNI actual.")
            else:
                i["DNI"] = nuevo_dni
        else:
            print("Ingrese un DNI válido. Se mantiene el DNI actual.")

    # Email
    print(f"Email actual: {i['Email']}")
    nuevo_email = input("Nuevo email (Enter para dejar igual): ")
    if nonempty(nuevo_email):
        nuevo_email = norm(nuevo_email)
        if "@" in nuevo_email:
            i["Email"] = nuevo_email
        else:
            print("Email inválido. Se mantiene el email actual.")

    # Teléfono
    print(f"Teléfono actual: {i['Telefono']}")
    raw_tel = input("Nuevo teléfono (solo números / Enter para dejar igual): ")
    raw_tel = norm(raw_tel)
    if nonempty(raw_tel):
        nuevo_tel = parse_int(raw_tel)
        if nuevo_tel is not None and nuevo_tel > 0:
            i["Telefono"] = nuevo_tel
        else:
            print("Ingrese un teléfono válido. Se mantiene el teléfono actual.")
    
    guardar_inquilinos(inquilinos)
    print ("\n✅ Inquilino modificado exitosamente.\n")
    return True
