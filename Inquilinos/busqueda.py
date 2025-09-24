from Inquilinos.datos import inquilinos
from FuncAux.validaciones import norm, nonempty, parse_int

def busqueda_inquilino():
    """
    Busca por nombre, apellido o ID dentro de `inquilinos`.
    - Muestra resultados y permite seleccionar uno por número de lista o por ID.
    - Retorna: (id_seleccionado, lista_ids_resultados)
      * id_seleccionado: int o None si no se seleccionó nada válido
      * lista_ids_resultados: list[int] con todos los IDs que matchearon
    """
    while True:  # reintentos
        termino = input("Ingrese nombre, apellido o ID a buscar: ")
        termino_norm = norm(termino)

        # Si ingresan un ID exacto, lo priorizamos como búsqueda directa
        posible_id = parse_int(termino_norm)
        if posible_id is not None:
            resultados_ids = [posible_id] if posible_id in inquilinos else []

        else:
            # Búsqueda por texto en Nombre / Apellido / Teléfono / Email
            resultados_ids = []
            for iid, i in inquilinos.items():
                texto = f"{i.get('Nombre','')} {i.get('Telefono','')} {i.get('Email','')}"
                if termino_norm in norm(texto):
                    resultados_ids.append(iid)

        if not resultados_ids:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
            continue

        # Mostrar resultados
        print("\nResultados encontrados:")
        for i, iid in enumerate(resultados_ids, start=1):
            i_data = inquilinos[iid]
            print(f"{i} - ID: {iid} | Nombre: {i_data['Nombre']} | Teléfono: {i_data['Telefono']} | Email: {i_data['Email']}")

        # Permitir selección por número de la lista o por ID
        opcion = norm(input("\nSeleccione el inquilino (número de la lista o ID): "))
        seleccionado_id = None

        # 1) Si eligió un número de la lista
        num_lista = parse_int(opcion)
        if num_lista is not None and 1 <= num_lista <= len(resultados_ids):
            seleccionado_id = resultados_ids[num_lista - 1]
        else:
            # 2) Si escribió un ID directamente
            id_directo = parse_int(opcion)  # Corregido aquí
            if id_directo in resultados_ids:
                seleccionado_id = id_directo
        
        if seleccionado_id is not None:
            i_data = inquilinos[seleccionado_id]
            return seleccionado_id, resultados_ids
        else:
            print("Opción inválida. Intente nuevamente.\n")
        