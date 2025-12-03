from FuncAux.busqueda_relacionada import contratos_por_inquilino
from Inquilinos.busqueda_inquilino import buscar_inquilinos, seleccionar_inquilino

def pagos_por_contrato(pagos, id_cto, parse_int):
    """
    Devuelve una lista con todos los pagos asociados a un contrato.
    """
    encontrados = []
    id_cto_int = parse_int(str(id_cto))

    for id_pago, datos in pagos.items():
        id_cto_pago = datos.get("ID Contrato")  # CON ESPACIO tal cual tu JSON
        id_pago_int = parse_int(str(id_cto_pago)) if id_cto_pago is not None else None

        if id_pago_int == id_cto_int:
            encontrados.append((id_pago, datos))

    return encontrados

def estadistica_pagos_por_inquilino(inquilinos, contratos, pagos, norm, parse_int):
    # 1) Buscar al inquilino
    resultados_ids = buscar_inquilinos(inquilinos, norm, parse_int)
    if not resultados_ids:
        print("No se seleccionó ningún inquilino.")
        return

    id_inq = seleccionar_inquilino(inquilinos, resultados_ids, norm)
    if id_inq is None:
        print("Cancelado.")
        return

    datos_inq = inquilinos.get(id_inq, {})
    nombre = datos_inq.get("Nombre", "(sin nombre)")

    print(f"\nInquilino seleccionado: [{id_inq}] {nombre}")

    # 2) Obtener contratos del inquilino
    contratos_inq = contratos_por_inquilino(contratos, id_inq, parse_int)
    if not contratos_inq:
        print("Este inquilino no tiene contratos.")
        return

    # 3) Para cada contrato, obtener sus pagos
    total_pagos = 0
    print("\nPagos por contrato:")

    for id_cto, datos_cto in contratos_inq:
        pagos_cto = pagos_por_contrato(pagos, id_cto, parse_int)
        cantidad = len(pagos_cto)
        total_pagos += cantidad
        print(f"- Contrato {id_cto}: {cantidad} pagos")

    print(f"\nTOTAL DE PAGOS DEL INQUILINO: {total_pagos}")
