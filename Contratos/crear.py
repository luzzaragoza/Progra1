def crear_matriz_contrato(cant_contratos):
    """
    Crea una matriz con contratos según la cantidad pedida.

    Formato de cada contrato:
    [ID Contrato, ID Propiedad, ID Inquilino, Fecha Inicio, Fecha Fin, Monto mensual, Estado]
    """
    contratos = []

    for i in range(cant_contratos):
        ID_contrato = len(contratos) + 1  

        id_propiedad = input("ID de la propiedad: ").strip()
        id_inquilino = input("ID del inquilino: ").strip()
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
        fecha_fin    = input("Fecha de fin (YYYY-MM-DD): ").strip()
        monto_mensual= input("Monto mensual: ").strip()

        contrato = [ID_contrato, id_propiedad, id_inquilino, fecha_inicio, fecha_fin, monto_mensual, True]

        contratos.append(contrato)

    return contratos
