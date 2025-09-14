import re

def validar_id(valor):
    """
    Valida que el ID sea un número entero positivo.
    """
    texto = str(valor).strip()
    return re.match(r"^[0-9]+$", texto) is not None

def validar_monto_mensual(valor):
    """
    Valida que el monto sea un número entero positivo.
    """
    texto = str(valor).strip()
    return re.match(r"^[0-9]+$", texto) is not None

def validar_fecha(valor):
    """
    Valida que la fecha tenga formato YYYY-MM-DD.
    No controla si el día/mes existen (solo formato).
    """
    texto = str(valor).strip()
    return re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", texto) is not None

def validar_contrato(fila, encabezados_contratos):
    """
    Verifica que la fila del contrato cumpla:
    [ID Contrato, ID Propiedad, ID Inquilino, Fecha Inicio, Fecha Fin, Monto]
    """
    i_id    = encabezados_contratos.index("ID Contrato")
    i_prop  = encabezados_contratos.index("ID Propiedad")
    i_inq   = encabezados_contratos.index("ID Inquilino")
    i_ini   = encabezados_contratos.index("Fecha Inicio")
    i_fin   = encabezados_contratos.index("Fecha Fin")
    i_monto = encabezados_contratos.index("Monto mensual")

    if not validar_id(fila[i_id]):      return False
    if not validar_id(fila[i_prop]):    return False
    if not validar_id(fila[i_inq]):     return False
    if not validar_fecha(fila[i_ini]):  return False
    if not validar_fecha(fila[i_fin]):  return False
    if not validar_monto_mensual(fila[i_monto]):return False

    return True
