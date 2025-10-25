import json
import os
from FuncAux.validaciones import norm, parse_int

def cargar_propiedades():
    ruta = os.path.join('Propiedades', 'datos.json')
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: El archivo datos.json está mal formateado.")
        return {}

def busqueda_propiedad():
    """
    Busca por dirección, tipo o ID dentro de `propiedades`.
    - Muestra resultados y permite seleccionar uno por número de lista o por ID.
    - Retorna: (id_seleccionado, lista_ids_resultados)
      * id_seleccionado: int o None si no se seleccionó nada válido
      * lista_ids_resultados: list[int] con todos los IDs que matchearon
    """
    propiedades = cargar_propiedades()
    
    while True:  # reintentos
        termino = input("Ingrese dirección, tipo o ID a buscar: ")
        termino_norm = norm(termino)

        # Si ingresan un ID exacto, lo priorizamos como búsqueda directa
        posible_id = parse_int(termino_norm)
        if posible_id is not None:
            resultados_ids = [posible_id] if posible_id in propiedades else []

        else:
            # Búsqueda por texto en Dirección / Tipo / Estado / Precio
            resultados_ids = []
            for pid, p in propiedades.items():
                texto = f"{p.get('Direccion','')} {p.get('Tipo','')} {p.get('Estado','')} {p.get('PrecioAlquiler','')}"
                if termino_norm in norm(texto):
                    resultados_ids.append(pid)

        if not resultados_ids:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
            continue

        # Mostrar resultados
        print("\nResultados encontrados:")
        for i, pid in enumerate(resultados_ids, start=1):
            p = propiedades[pid]
            print(f"{i} - ID: {pid} | Dirección: {p['Direccion']} | Tipo: {p['Tipo']} | Precio: {p['PrecioAlquiler']} | Estado: {p['Estado']}")

        # Permitir selección por número de la lista o por ID
        opcion = norm(input("\nSeleccione la propiedad (número de la lista o ID): "))
        seleccionado_id = None

        # 1) Si eligió un número de la lista
        num_lista = parse_int(opcion)
        if num_lista is not None and 1 <= num_lista <= len(resultados_ids):
            seleccionado_id = resultados_ids[num_lista - 1]
        else:
            # 2) Si escribió un ID directamente
            id_directo = parse_int(opcion)
            if id_directo in resultados_ids:
                seleccionado_id = id_directo

        if seleccionado_id is not None:
            p = propiedades[seleccionado_id]
            return seleccionado_id, resultados_ids
        else:
            print("Opción inválida. Intente nuevamente.\n")
