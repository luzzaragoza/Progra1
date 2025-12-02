import json
import os
from Inquilinos.busqueda_inquilino import buscar_inquilinos, seleccionar_inquilino
from FuncAux.validaciones import norm, nonempty, parse_int


def cargar_inquilinos():
    ruta = 'Inquilinos/datos_inquilino.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_inquilinos(inquilinos):
    ruta = 'Inquilinos/datos_inquilinos.json'  
    with open(ruta, 'w', encoding='utf-8') as f:
        json.dump(inquilinos, f, indent=2, ensure_ascii=False)

def modificar_inquilino():
    print("----- Modificar Inquilino -----")

    # 0) Cargar base actual
    inquilinos = cargar_inquilinos()

    # 1) Buscar con reintentos (tu función tal cual)
    resultados_ids = buscar_inquilinos(inquilinos, norm, parse_int)
    if not resultados_ids:
        print("Búsqueda cancelada.\n")
        return False

    # 2) Seleccionar uno de la lista (tu función tal cual)
    id_inq = seleccionar_inquilino(inquilinos, resultados_ids, norm)
    if id_inq is None:
        print("Modificación cancelada.\n")
        return False

    # 3) Verificar que siga existiendo y tomar referencia
    if id_inq not in inquilinos:
        print("❌ Inquilino no encontrado (fue eliminado o inconsistente).\n")
        return False

    i = inquilinos[id_inq]

    # 4) Tomar snapshot de valores actuales para el resumen
    try:
        old_nombre = i.get("Nombre", "")
    except (KeyError, AttributeError):
        old_nombre = "[Error de lectura]"

    try:
        old_dni = i.get("DNI", "")
    except (KeyError, AttributeError):
        old_dni = "[Error de lectura]"

    try:
        old_email = i.get("Email", "")
    except (KeyError, AttributeError):
        old_email = "[Error de lectura]"

    try:
        old_tel = i.get("Telefono", "")
    except (KeyError, AttributeError):
        old_tel = "[Error de lectura]"

    cambios = {}  # {'Campo': (antes, despues)}

    # 5) Edición de campos (misma lógica tuya, anotando cambios)

    # Nombre
    try:
        print(f"\nNombre actual: {i['Nombre']}")
    except (KeyError, AttributeError):
        print("\n[Error en lectura de Nombre actual]")

    nuevo_nombre = input("Nuevo nombre (Enter para dejar igual): ")
    if nonempty(nuevo_nombre):
        try:
            i["Nombre"] = norm(nuevo_nombre)
            if i.get("Nombre", "") != old_nombre:
                cambios["Nombre"] = (old_nombre, i.get("Nombre", ""))
        except (KeyError, AttributeError):
            print("No se pudo actualizar el Nombre (error de estructura).")

    # DNI
    try:
        print(f"DNI actual: {i['DNI']}")
    except (KeyError, AttributeError):
        print("[Error en lectura de DNI actual]")

    raw_dni = input("Nuevo DNI (solo números / Enter para dejar igual): ")
    raw_dni = norm(raw_dni)
    if nonempty(raw_dni):
        nuevo_dni = parse_int(raw_dni)
        if nuevo_dni is not None and nuevo_dni > 0:
            # validar unicidad en otros inquilinos
            repetido = False
            for inq_id, inq in inquilinos.items():
                try:
                    if inq_id != id_inq and inq.get("DNI") == nuevo_dni:
                        repetido = True
                        break
                except (KeyError, AttributeError):
                    continue
            if repetido:
                print("Ese DNI ya está registrado a otro inquilino. Se mantiene el DNI actual.")
            else:
                try:
                    i["DNI"] = nuevo_dni
                    if i.get("DNI", "") != old_dni:
                        cambios["DNI"] = (old_dni, i.get("DNI", ""))
                except (KeyError, AttributeError):
                    print("No se pudo actualizar el DNI (error de estructura).")
        else:
            print("Ingrese un DNI válido. Se mantiene el DNI actual.")

    # Email
    try:
        print(f"Email actual: {i['Email']}")
    except (KeyError, AttributeError):
        print("[Error en lectura de Email actual]")

    nuevo_email = input("Nuevo email (Enter para dejar igual): ")
    if nonempty(nuevo_email):
        nuevo_email = norm(nuevo_email)
        if "@" in nuevo_email:
            try:
                i["Email"] = nuevo_email
                if i.get("Email", "") != old_email:
                    cambios["Email"] = (old_email, i.get("Email", ""))
            except (KeyError, AttributeError):
                print("No se pudo actualizar el Email (error de estructura).")
        else:
            print("Email inválido. Se mantiene el email actual.")

    # Teléfono
    try:
        print(f"Teléfono actual: {i['Telefono']}")
    except (KeyError, AttributeError):
        print("[Error en lectura de Teléfono actual]")

    raw_tel = input("Nuevo teléfono (solo números / Enter para dejar igual): ")
    raw_tel = norm(raw_tel)
    if nonempty(raw_tel):
        nuevo_tel = parse_int(raw_tel)
        if nuevo_tel is not None and nuevo_tel > 0:
            try:
                i["Telefono"] = nuevo_tel
                if i.get("Telefono", "") != old_tel:
                    cambios["Telefono"] = (old_tel, i.get("Telefono", ""))
            except (KeyError, AttributeError):
                print("No se pudo actualizar el Teléfono (error de estructura).")
        else:
            print("Ingrese un teléfono válido. Se mantiene el teléfono actual.")

    # 6) Guardar cambios
    guardar_inquilinos(inquilinos)

    # 7) Resumen de cambios
    if cambios:
        print("\nCambios realizados:")
        for k in ["Nombre", "DNI", "Email", "Telefono"]:
            if k in cambios:
                antes, despues = cambios[k]
                print(f" - {k}: {antes}  →  {despues}")
    else:
        print("\nNo se realizaron cambios en los datos.")

    print("\n✅ Inquilino modificado exitosamente.\n")
    return True
