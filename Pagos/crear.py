ultimo_id_pago = 0  

def crear_matriz_pagos(cant_pagos, pagos_existentes=None):
    global ultimo_id_pago
    
    if pagos_existentes is None:
        pagos_existentes = []
    
    pagos = pagos_existentes[:]
    
    for i in range(cant_pagos):
        ultimo_id_pago += 1
        ID_pago = ultimo_id_pago
        id_contrato = int(input("ID del contrato: "))
        fecha_pago = input("Fecha de pago (YYYY-MM-DD): ")
        monto = int(input("Monto del pago: "))

        print("Seleccione el método de pago:")
        print("1 - Tarjeta")
        print("2 - Efectivo")
        print("3 - Transferencia")
        opcion = input("Opción: ")

        if opcion == "1":
            metodo = "Tarjeta"
        elif opcion == "2":
            metodo = "Efectivo"
        elif opcion == "3":
            metodo = "Transferencia"
        else:
            print("Opción inválida. Se registrará como 'Otro'.")
            metodo = "Otro"

        pago = [ID_pago, id_contrato, fecha_pago, monto, metodo]
        pagos.append(pago)

    return pagos