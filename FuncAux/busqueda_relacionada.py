from Inquilinos.busqueda_inquilino import buscar_inquilinos, seleccionar_inquilino
from FuncAux.validaciones import parse_int, norm 
import json

def contratos_por_inquilino(contratos, id_inq, parse_int):
    """
    Devuelve lista de (id_contrato, datos_contrato)
    donde 'ID Inquilino' coincide con id_inq.
    """
    encontrados = []

    # Normalizamos el ID buscado
    id_busq_int = parse_int(str(id_inq))

    for id_contrato, datos in contratos.items():
        id_inq_cto = datos.get("ID_Inquilino")

        # Normalizar posible ID del contrato
        id_cto_int = parse_int(str(id_inq_cto)) if id_inq_cto is not None else None

        if id_busq_int is not None and id_cto_int is not None and id_busq_int == id_cto_int:
            encontrados.append((id_contrato, datos))

    return encontrados

def cargar_inquilinos():
    ruta = 'Inquilinos/datos_inquilino.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def cargar_propiedades():
    ruta = 'Propiedades/datos_propiedad.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def cargar_contratos():
    ruta = 'Contratos/datos_contrato.json' 
    with open(ruta, 'r', encoding='utf-8') as f:
        return json.load(f)

def obtener_propiedad(propiedades, id_prop, parse_int):
    """
    Devuelve el dict de una propiedad por ID, tolerando int/str.
    """
    if id_prop is None:
        return None

    # 1) probar con la clave tal cual viene
    if id_prop in propiedades:
        return propiedades[id_prop]

    # 2) probar con string
    id_str = str(id_prop)
    if id_str in propiedades:
        return propiedades[id_str]

    # 3) probar con int
    id_int = parse_int(str(id_prop))
    if id_int is not None and id_int in propiedades:
        return propiedades[id_int]

    # 4) si nada funcionó → no se encontró
    return None



def busqueda_relacionada_inq(inquilinos, propiedades, contratos):
    """
    Flujo completo:
    - Busca inquilinos
    - Usuario selecciona uno (usa tu seleccionar_inquilino)
    - Muestra contratos asociados
    - Muestra dirección de la propiedad asociada
    """

    print("----- Búsqueda de Contratos por Inquilino -----")

    # 1) Buscar lista de IDs
    resultados_ids = buscar_inquilinos(inquilinos, norm, parse_int)
    if not resultados_ids:
        print("No se encontró ningún inquilino.")
        return

    # 2) Dejar elegir un solo inquilino
    id_inq = seleccionar_inquilino(inquilinos, resultados_ids, norm)
    if id_inq is None:
        print("Operación cancelada.")
        return

    datos_inq = inquilinos.get(id_inq, {})
    nombre = datos_inq.get("Nombre", "(sin nombre)")

    print(f"\nInquilino seleccionado: [{id_inq}] {nombre}")

    # 3) Obtener todos sus contratos
    contratos_rel = contratos_por_inquilino(contratos, id_inq, parse_int)
    if not contratos_rel:
        print("Este inquilino no tiene contratos asociados.")
        return

    # 4) Mostrar cada contrato con su propiedad
    print("\nContratos relacionados:")
    for id_cto, datos_cto in contratos_rel:
        id_prop = datos_cto.get("ID_Propiedad")
        prop = obtener_propiedad(propiedades, id_prop, parse_int)

        if prop is None:
            direccion = "Propiedad no encontradaa"
        else:
            direccion = prop.get("Direccion", "(sin dirección)")

        print(f"- Contrato [{id_cto}] → Propiedad [{id_prop}] — Dirección: {direccion}")
