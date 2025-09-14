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

            # Diccionario de métodos de pago
            metodos = {
                "1": "Tarjeta",
                "2": "Efectivo",
                "3": "Transferencia"
            }

            print("Seleccione el nuevo método de pago (o Enter para no modificar):")
            for k, v in metodos.items():
                print(f"{k} - {v}")

            opcion = input("Opción: ").strip()
            if opcion in metodos:
                pago[4] = metodos[opcion]
            elif opcion == "":
                pass  # No modifica el método
            else:
                print("Opción inválida. El método no se modificará.")

            print("Pago modificado exitosamente.")
            return
    print("Pago no encontrado.")
