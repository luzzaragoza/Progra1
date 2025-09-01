def crear_matriz_contrato(cant_contratos):
    contratos=[]
    for i in range(cant_contratos):
        ID_contrato= len(contratos) + 1
        id_propiedad=int(input("ID de la propiedad:"))
        id_inquilino=int(input("ID del inquilino:"))
        fecha_inicio=input("Fecha de inicio (YYYY-MM-DD):")
        fecha_fin=input("Fecha de fin (YYYY-MM-DD):")

        contrato=[id_propiedad, id_inquilino, fecha_inicio, fecha_fin]
        contratos.append(contrato)

    return contratos
