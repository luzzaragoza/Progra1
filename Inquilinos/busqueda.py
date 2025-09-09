
""""
import re
from validaciones import validar_id, validar_nombre, validar_dni, validar_email, validar_telefono

def detectar_tipo(dato):
    s = str(dato).strip()
    if validar_dni(s):       return "DNI"     # DNI antes que ID porque es un formato especifico además permite no confundir ID con DNI (que id no se considere un dni)
    if validar_id(s):        return "ID"
    if validar_email(s):     return "EMAIL"
    if validar_telefono(s):  return "TEL"
    if validar_nombre(s):    return "NOMBRE"
    return ""  # no coincide con ningún formato

def pedir_confirmacion(tipo, dato):
    print("Voy a buscar por", tipo, "=", dato)
    resp = input("¿Confirmás? (s/n): ").strip().lower()
    if resp == "s" or resp == "si" or resp == "sí":
        return True
    else:
        return False

def buscar_inquilino(dato, tipo, matriz):		# buscar_inquilino(dato, tipo, matriz): recibe un dato a buscar y su tipo validado ("ID"/"DNI"/"EMAIL"/"TEL"/"NOMBRE") sobre una matriz sin encabezados [ID, Nombre, DNI, Email, Tel] y devuelve True si existe al menos una coincidencia, o False si no.

    # Robustez básica
    if matriz is None or len(matriz) == 0:
        return False

    s = str(dato).strip()
    if s == "":
        return False

    # Selectores de columna (índices fijos: [ID, Nombre, DNI, Email, Tel])
    col_id      = lambda m: [str((f[0] if len(f) > 0 else "")).strip() for f in m]
    col_nombre  = lambda m: [str((f[1] if len(f) > 1 else "")).strip() for f in m]
    col_dni     = lambda m: [str((f[2] if len(f) > 2 else "")).strip() for f in m]
    col_email   = lambda m: [str((f[3] if len(f) > 3 else "") or "").strip() for f in m]
    col_telefono= lambda m: [str((f[4] if len(f) > 4 else "") or "") for f in m]

    # Comparadores por tipo
    comparar_igual        = lambda valor, celda: re.search(rf"^{re.escape(valor)}$", celda) is not None
    comparar_igual_ci     = lambda valor, celda: re.search(rf"^{re.escape(valor)}$", celda, flags=re.IGNORECASE) is not None
    comparar_telefono     = lambda valor, celda: re.findall(r"\d", valor) == re.findall(r"\d", celda)
    comparar_subcadena_ci = lambda valor, celda: re.search(re.escape(valor), celda, flags=re.IGNORECASE) is not None

    # Elegir columna y regla según el tipo (sin diccionarios)
    if tipo == "ID":
        columna = col_id(matriz)
        coincide = lambda celda: comparar_igual(s, celda)
    elif tipo == "DNI":
        columna = col_dni(matriz)
        coincide = lambda celda: comparar_igual(s, celda)
    elif tipo == "EMAIL":
        columna = col_email(matriz)
        coincide = lambda celda: comparar_igual_ci(s, celda)
    elif tipo == "TEL":
        columna = col_telefono(matriz)
        coincide = lambda celda: comparar_telefono(s, celda)
    elif tipo == "NOMBRE":
        columna = col_nombre(matriz)
        coincide = lambda celda: comparar_subcadena_ci(s, celda)
    else:
        return False

    # Recorrido sin any(): cortar apenas encuentra
    i = 0
    while i < len(columna):
        if coincide(columna[i]):
            return True
        i += 1
    return False

    """""

def busqueda_inquilino(matriz):
    while True:  # Bucle para reintentos
        termino = input("Ingrese nombre, DNI, email o teléfono del inquilino a buscar: ").lower()
        resultados = [inq for inq in matriz if termino in f"{inq[1]} {inq[2]} {inq[3]} {inq[4]}".lower()]

        if not resultados:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i, inq in enumerate(resultados, start=1):
                print(f"{i} - ID: {inq[0]} | Nombre: {inq[1]} | DNI: {inq[2]} | Email: {inq[3]} | Tel: {inq[4]} | Estado: {inq[5]}")

            opcion = input("\nSeleccione el inquilino (número de la lista o ID): ").lower()
            seleccionado = None

            for i, inq in enumerate(resultados, start=1):
                if opcion == str(i) or opcion == str(inq[0]):
                    print("\nHas seleccionado:")
                    print(f"ID: {inq[0]} | Nombre: {inq[1]} | DNI: {inq[2]} | Email: {inq[3]} | Tel: {inq[4]} | Estado: {inq[5]}")
                    seleccionado = inq
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")
