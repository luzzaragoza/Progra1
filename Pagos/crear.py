def crear_matriz_pagos(cant_pagos):
    pagos=[]
    for i in range(cant_pagos):
        ID_pago= len(pagos) + 1
        id_contrato=int(input("ID del contrato:"))
        fecha_pago=input("Fecha de pago (YYYY-MM-DD):")
        monto=int(input("Monto del pago:"))
        metodo=input("Metodo de pago:")

        pago=[ID_pago, id_contrato, fecha_pago, monto, metodo]
        pagos.append(pago)

    return pagos
