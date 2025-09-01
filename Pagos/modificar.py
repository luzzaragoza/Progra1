
def modificar_pago(matriz):
    id_pago = int(input("Ingrese el ID del pago a modificar: "))
    for pago in matriz:
        if pago[0] == id_pago:
            id_contrato = input("Nuevo ID de contrato: ")
            if id_contrato:
                pago[1] = int(id_contrato)
            fecha_pago = input("Nueva fecha de pago (YYYY-MM-DD): ")
            if fecha_pago:
                pago[2] = fecha_pago
            monto = input("Nuevo monto: ")
            if monto:
                pago[3] = int(monto)
            metodo = input("Nuevo método de pago: ")
            if metodo:
                pago[4] = metodo

            print("Pago modificado exitosamente.")
            return
    print("Pago no encontrado.")
