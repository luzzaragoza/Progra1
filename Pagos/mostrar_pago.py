import json
import os

def cargar_pagos():
    ruta = 'Pagos/datos_pago.json'  
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def mostrar_pagos():
    print("\n--- Lista de Pagos ---")
    pagos = cargar_pagos()
    
    if not pagos:
        print("No hay pagos registrados.\n")
        return

    for id_pago, detalles in pagos.items():
        print(f"ID Pago: {id_pago}")
        for clave, valor in detalles.items():
            print(f"  {clave}: {valor}")
        print("-" * 20)
