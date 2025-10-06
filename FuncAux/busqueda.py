from FuncAux.validaciones import norm, parse_int

def busqueda_por_id(entidad):
    """
    Busca en una entiedad por un ID exacto.
    """
    resultados = []
    while True:
        id_buscado = input(f"Ingrese el ID de {entidad} a buscar: ")
        id_buscado_int = parse_int(id_buscado)
        if id_buscado_int is None or id_buscado_int <= 0:
            print("ID inválido. Intente nuevamente.\n")
            continue
        if id_buscado_int in entidad:
            resultados.append(id_buscado_int)
            return resultados
        else:
            print(f"No se encontró {entidad} con ID {id_buscado_int}. Intente nuevamente.\n")



