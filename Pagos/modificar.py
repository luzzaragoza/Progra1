def modificar_pago(matriz):
    id_pago = int(input("Ingrese el ID del pago a modificar: "))
    for pago in matriz:
        if pago[0] == id_pago:
            id_contrato = input("Nuevo ID de contrato (Enter para no modificar): ")
            if id_contrato:
                pago[1] = int(id_contrato)

            fecha_pago = input("Nueva fecha de pago (YYYY-MM-DD, Enter para no modificar): ")
            if fecha_pago:
                pago[2] = fecha_pago

            monto = input("Nuevo monto (Enter para no modificar): ")
            if monto:
                pago[3] = int(monto)

            print("Seleccione el nuevo método de pago (o Enter para no modificar):")
            print("1 - Tarjeta")
            print("2 - Efectivo")
            print("3 - Transferencia")
            opcion = input("Opción: ")
            if opcion == "1":
                pago[4] = "Tarjeta"
            elif opcion == "2":
                pago[4] = "Efectivo"
            elif opcion == "3":
                pago[4] = "Transferencia"
            elif opcion.strip() == "":
                pass  # No modifica el método si se deja vacío
            else:
                print("Opción inválida. El método no se modificará.")

            print("Pago modificado exitosamente.")
            return
    print("Pago no encontrado.")
