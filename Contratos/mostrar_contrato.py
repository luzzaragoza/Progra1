import json
import os

def cargar_json(ruta_carpeta):
    nombre_archivo = f'datos_{ruta_carpeta.lower()}.json'
    ruta = f'{ruta_carpeta}/{nombre_archivo}'
    if not os.path.exists(ruta):
        return {}
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def mostrar_contratos():
    contratos = cargar_json('Contratos')
    inquilinos = cargar_json('Inquilinos')
    propiedades = cargar_json('Propiedades')

    if not contratos:
        print("No hay contratos para mostrar.\n")
        return

    #filtrar solo contratos "activos"
    contratos_activos = list(
        filter(lambda c: c.get("Estado", "").lower() == "activo", contratos.values())
    )

    print("Contratos activos (filter aplicado):")
    for c in contratos_activos:
        print(f"  - ID Inquilino {c.get('ID_Inquilino')} | Propiedad {c.get('ID_Propiedad')}")
    print()

    print("----- Lista de Contratos -----")
    for id_contrato, c in contratos.items():
        id_inquilino = str(c.get("ID_Inquilino", ""))
        id_propiedad = str(c.get("ID_Propiedad", ""))

        # Buscar el nombre del inquilino y direccion de la propiedad
        inquilino_data = inquilinos.get(id_inquilino, {})
        propiedad_data = propiedades.get(id_propiedad, {})
        
        nombre_inquilino = inquilino_data.get("Nombre", "Inexistente")
        calle_propiedad = propiedad_data.get("Direccion", "Inexistente")

        print(f"ID Contrato: {id_contrato}")
        print(f"  Inquilino (ID: {id_inquilino}): {nombre_inquilino}")
        print(f"  Propiedad (ID: {id_propiedad}): {calle_propiedad}")
        print(f"  Monto Mensual: ${c['Monto']}")
        print(f"  Fecha Inicio: {c['Fecha_Inicio']}")
        print(f"  Fecha Fin: {c['Fecha_Fin']}")
        print(f"  Estado: {c['Estado']}")
        print("------------------------------")
    print()
