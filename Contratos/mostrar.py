import json
import os

def cargar_json(ruta_carpeta):
    ruta = os.path.join(ruta_carpeta, 'datos.json')
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

    print("----- Lista de Contratos -----")
    for id_contrato, c in contratos.items():
        id_inquilino = str(c.get("ID_Inquilino", ""))
        id_propiedad = str(c.get("ID_Propiedad", ""))

        nombre_inquilino = inquilinos.get(id_inquilino, {}).get("Nombre", "Desconocido")
        calle_propiedad = propiedades.get(id_propiedad, {}).get("Direccion", "Desconocida")

        print(f"ID Contrato: {id_contrato}")
        print(f"  Inquilino: {nombre_inquilino}")
        print(f"  Propiedad: {calle_propiedad}")
        print(f"  Monto Mensual: ${c['Monto']}")
        print(f"  Fecha Inicio: {c['Fecha_Inicio']}")
        print(f"  Fecha Fin: {c['Fecha_Fin']}")
        print(f"  Estado: {c['Estado']}")
        print("------------------------------")
    print()
