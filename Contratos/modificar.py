
def modificar_contrato(matriz):
    id_contrato = int(input("Ingrese el ID del contrato a modificar: "))
    for contrato in matriz:
        if contrato[0] == id_contrato:
            id_propiedad = input("Nuevo ID de propiedad: ")
            if id_propiedad:
                contrato[1] = int(id_propiedad)
            id_inquilino = input("Nuevo ID de inquilino: ")
            if id_inquilino:
                contrato[2] = int(id_inquilino)
            fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ")
            if fecha_inicio:
                contrato[3] = fecha_inicio
            fecha_fin = input("Nueva fecha de fin (YYYY-MM-DD): ")
            if fecha_fin:
                contrato[4] = fecha_fin
            if monto: 
                monto = int(input("Nuevo monto mensual (entero): ")) 
                contrato[5] = monto

            print("Contrato modificado exitosamente.")
            return
    print("Contrato no encontrado.")


