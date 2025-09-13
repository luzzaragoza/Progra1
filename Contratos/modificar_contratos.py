from .validaciones_contratos import validar_id, validar_fecha, validar_monto_mensual

# posiciones en la lista contrato (constantes globales)
POS_ID        = 0
POS_PROPIEDAD = 1
POS_INQUILINO = 2
POS_FECHA_INI = 3
POS_FECHA_FIN = 4
POS_MONTO     = 5

def _editar_campo(contrato, indice, mensaje, validador, convertir=lambda x: x): #puse una funcion mas porque tiene que estar modularizado tambien a nivel logico los archivos
    """
    Pide un valor, lo valida y lo guarda en contrato[indice].
    ENTER = mantener el valor actual.
    """
    entrada = input(mensaje).strip()
    if not entrada:
        return False
    if not validador(entrada):
        print("Valor inválido. No se aplicó cambio.")
        return False
    contrato[indice] = convertir(entrada)
    return True

def modificar_contrato(matriz):
    """
    Modifica un contrato existente buscándolo por ID.
    Permite editar propiedad, inquilino, fechas y monto mensual.
    ENTER en un campo = mantener el valor actual.
    """
    entrada = input("ID del contrato a modificar: ").strip() 
    if not validar_id(entrada):
        print("ID inválido.")
        return
    id_contrato = int(entrada)

    for contrato in matriz:
        if contrato[POS_ID] == id_contrato:
            _editar_campo(contrato, POS_PROPIEDAD, "Nuevo ID Propiedad (ENTER = igual): ", validar_id, int)
            _editar_campo(contrato, POS_INQUILINO, "Nuevo ID Inquilino (ENTER = igual): ", validar_id, int)
            _editar_campo(contrato, POS_FECHA_INI, "Nueva Fecha Inicio (YYYY-MM-DD, ENTER = igual): ", validar_fecha, str)
            _editar_campo(contrato, POS_FECHA_FIN, "Nueva Fecha Fin (YYYY-MM-DD, ENTER = igual): ", validar_fecha, str)
            _editar_campo(contrato, POS_MONTO, "Nuevo Monto (entero, ENTER = igual): ", validar_monto_mensual, int)

            print("Contrato modificado exitosamente.")
            return

    print("Contrato no encontrado.")


