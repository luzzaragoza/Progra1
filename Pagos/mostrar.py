from Pagos.datos import pagos

def mostrar_pagos():
    print("\n--- Lista de Pagos ---")
    if not pagos:
        print("No hay pagos registrados.\n")
        return

    for id_pago, detalles in pagos.items():
        print(f"ID Pago: {id_pago}")
        for clave, valor in detalles.items():
            print(f"  {clave}: {valor}")
        print("-" * 20)
        