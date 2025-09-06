import re

def validar_id(valor):
    texto = str(valor).strip()
    coincide = re.match(r"^[0-9]+$", texto)
    if coincide is None:
        return False
    else:
        return True

def validar_nombre(valor):
    texto = str(valor).strip()
    coincide = re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]{2,60}$", texto)
    if coincide is None:
        return False
    else:
        return True

def validar_dni(valor):
    texto = str(valor).strip()
    coincide = re.match(r"^[0-9]{7,8}$", texto)
    if coincide is None:
        return False
    else:
        return True


def validar_telefono(valor):
    texto = str(valor)
    solo_dig = re.findall(r"[0-9]", texto)
    cantidad = len(solo_dig)
    if cantidad >= 6 and cantidad <= 15:
        return True
    else:
        return False

def validar_inquilino(fila, encabezados_inquilinos):               #para verificar si los inquilinos están bien subidos
    i_id  = encabezados_inquilinos.index("ID Inquilino")
    i_nom = encabezados_inquilinos.index("Nombre")
    i_dni = encabezados_inquilinos.index("DNI")
    i_tel = encabezados_inquilinos.index("Teléfono")

    if not validar_id(fila[i_id]):
        return False
    if not validar_nombre(fila[i_nom]):
        return False
    if not validar_dni(fila[i_dni]):
        return False
    if not validar_telefono(fila[i_tel]):
        return False

    return True