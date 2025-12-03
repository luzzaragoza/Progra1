import json
from functools import reduce
import re
from FuncAux.validaciones import validar_dni, norm, parse_int
from FuncAux.estadistica_relacionada import estadistica_pagos_por_inquilino

def cargar_inquilinos():
    """Carga los inquilinos desde el archivo JSON."""
    ruta = 'Inquilinos/datos_inquilino.json'
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

def cargar_propiedades():
    """Carga las propiedades desde el archivo JSON."""
    ruta = 'Propiedades/datos_propiedad.json'
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

def cargar_contratos():
    """Carga los contratos desde el archivo JSON."""
    ruta = 'Contratos/datos_contrato.json'
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

def cargar_pagos():
    """Carga los pagos desde el archivo JSON."""
    ruta = 'Pagos/datos_pago.json'
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

def contar_por_estado_recursivo(propiedades_dict, estado_buscado, claves=None):
    """
    Cuenta recursivamente cuántas propiedades tienen un estado específico.
    Usa recursividad para recorrer las claves del diccionario.
    """
    if claves is None:
        claves = list(propiedades_dict.keys())
    
    # Caso base: no hay más claves
    if len(claves) == 0:
        return 0
    
    # Tomar la primera clave y procesar recursivamente el resto
    primera_clave = claves[0]
    resto_claves = claves[1:]
    
    propiedad = propiedades_dict[primera_clave]
    cuenta_actual = 1 if propiedad.get('Estado') == estado_buscado else 0
    
    # Llamada recursiva con el resto de claves
    return cuenta_actual + contar_por_estado_recursivo(propiedades_dict, estado_buscado, resto_claves)

def contar_contratos_estado_recursivo(contratos_dict, estado_buscado, claves=None):
    """
    Cuenta recursivamente cuántos contratos tienen un estado específico.
    Usa recursividad para recorrer las claves del diccionario.
    """
    if claves is None:
        claves = list(contratos_dict.keys())
    
    # Caso base: no hay más claves
    if len(claves) == 0:
        return 0
    
    # Tomar la primera clave y procesar recursivamente el resto
    primera_clave = claves[0]
    resto_claves = claves[1:]
    
    contrato = contratos_dict[primera_clave]
    cuenta_actual = 1 if contrato.get('Estado') == estado_buscado else 0
    
    # Llamada recursiva con el resto de claves
    return cuenta_actual + contar_contratos_estado_recursivo(contratos_dict, estado_buscado, resto_claves)

def sumar_montos_recursivo(pagos_lista, metodo_buscado, indice=0):
    """
    Suma recursivamente los montos de pagos con un método específico.
    Usa recursividad sobre una lista de pagos.
    """
    # Caso base: llegamos al final de la lista
    if indice >= len(pagos_lista):
        return 0
    
    pago = pagos_lista[indice]
    monto_actual = float(pago.get('Monto', 0)) if pago.get('Método') == metodo_buscado else 0
    
    # Llamada recursiva con el siguiente índice
    return monto_actual + sumar_montos_recursivo(pagos_lista, metodo_buscado, indice + 1)

def estadisticas_propiedades():
    """Muestra estadísticas de propiedades."""
    propiedades = cargar_propiedades()
    
    if len(propiedades) == 0:
        print("\nNo hay propiedades registradas.")
        return
    
    total = 0
    ocupados = 0
    libres = 0
    casas = 0
    departamentos = 0
    
    for id_propiedad in propiedades:
        propiedad = propiedades[id_propiedad]
        total = total + 1
        
        if propiedad['Estado'] == 'Ocupado':
            ocupados = ocupados + 1
        elif propiedad['Estado'] == 'Disponible':
            libres = libres + 1
        
        if propiedad['Tipo'] == 'Casa':
            casas = casas + 1
        elif propiedad['Tipo'] == 'Departamento':
            departamentos = departamentos + 1
    
    ocupados_recursivo = contar_por_estado_recursivo(propiedades, 'Ocupado')
    libres_recursivo = contar_por_estado_recursivo(propiedades, 'Disponible')
    
    print("\n----- Estadísticas de Propiedades -----")
    print("Total de inmuebles:", total)
    print("Inmuebles ocupados:", ocupados_recursivo)
    print("Inmuebles libres:", libres_recursivo)
    print("Cantidad de casas:", casas)
    print("Cantidad de departamentos:", departamentos)
    print()

def estadisticas_pagos():
    """Muestra estadísticas de métodos de pago."""
    pagos = cargar_pagos()
    
    if not pagos:
        print("\nNo hay pagos registrados.")
        return

    # usamos .values() porque no necesitamos el ID
    valores = pagos.values()

    efectivo = len(list(filter(lambda p: p["Método"] == "Efectivo", valores)))
    tarjeta = len(list(filter(lambda p: p["Método"] in ("Tarjeta", "Débito"), valores)))
    transferencia = len(list(filter(lambda p: p["Método"] == "Transferencia", valores)))

    print("\n----- Estadísticas de Pagos -----")
    print("Pagos en efectivo:", efectivo)
    print("Pagos con tarjeta:", tarjeta)
    print("Pagos por transferencia:", transferencia)
    print()


def estadisticas_contratos():
    """Muestra estadísticas de contratos."""
    contratos = cargar_contratos()
    
    if not contratos:
        print("\nNo hay contratos registrados.")
        return

    valores = contratos.values()

    vigentes = len(list(filter(lambda c: c["Estado"] == "Vigente", valores)))
    finalizados = len(list(filter(lambda c: c["Estado"] == "Finalizado", valores)))
    
    vigentes_recursivo = contar_contratos_estado_recursivo(contratos, 'Vigente')
    finalizados_recursivo = contar_contratos_estado_recursivo(contratos, 'Finalizado')

    print("\n----- Estadísticas de Contratos -----")
    print("Contratos vigentes:", vigentes_recursivo)
    print("Contratos dados de baja:", finalizados_recursivo)
    print()

def total_por_metodo(metodo):
    """Devuelve el total de montos de pagos según el método indicado."""
    pagos = cargar_pagos()
    if not pagos:
        print("\nNo hay pagos registrados.")
        return 0

    # valores del diccionario (sin IDs)
    valores = list(pagos.values())

    total_recursivo = sumar_montos_recursivo(valores, metodo)

    # filtramos solo los del método indicado
    filtrados = filter(lambda p: p["Método"] == metodo, valores)

    # convertimos montos a float por si vinieran como str
    montos = map(lambda p: float(p["Monto"]), filtrados)

    # acumulamos la suma total
    total = reduce(lambda acc, m: acc + m, montos, 0)

    print(f"💰 Total en {metodo}: ${total_recursivo:,.2f}")
    return total_recursivo



def estadistica_dominios_email(inquilinos):
    """Genera estadísticas de dominios de email usando expresiones regulares."""
    patron = r"@([a-zA-Z0-9.-]+)$"   # captura el dominio del email
    
    dominios = {}                    # diccionario {dominio: cantidad}

    for iid, datos in inquilinos.items():
        email = str(datos.get("Email", "")).strip()

        m = re.search(patron, email)

        if m:
            dominio = m.group(1)    # ejemplo: "gmail.com"
        else:
            dominio = "(email inválido)"

        # contamos a mano
        if dominio in dominios:
            dominios[dominio] += 1
        else:
            dominios[dominio] = 1

    # Mostrar el resultado
    print("\n--- Estadística de dominios de email ---")
    for dominio, cantidad in sorted(dominios.items(), key=lambda x: x[1], reverse=True):
        print(f"{dominio:20} → {cantidad} inquilinos")

    return dominios

def estadistica_dni_inquilinos(inquilinos):
    """
    Estadística completa:
    - DNI válidos
    - DNI inválidos
    - Porcentajes
    - Detalle de los inválidos
    """
    validos = 0
    invalidos = 0
    invalidos_detalle = []

    for iid, datos in inquilinos.items():
        dni = str(datos.get("DNI", "")).strip()

        if validar_dni(dni):
            validos += 1
        else:
            invalidos += 1
            nombre = datos.get("Nombre", "(sin nombre)")
            invalidos_detalle.append((iid, nombre, dni))

    total = validos + invalidos

    print("\n--- Estadística de DNI de Inquilinos ---")
    print(f"Total de inquilinos:    {total}")
    print(f"DNI válidos:            {validos}")
    print(f"DNI inválidos:          {invalidos}")

    if total > 0:
        porc_validos = validos * 100 / total
        porc_invalidos = invalidos * 100 / total
        print(f"Porcentaje válidos:     {porc_validos:.2f}%")
        print(f"Porcentaje inválidos:   {porc_invalidos:.2f}%")

    if invalidos_detalle:
        print("\nInquilinos con DNI inválido:")
        for iid, nombre, dni in invalidos_detalle:
            print(f"- ID {iid} | {nombre} | DNI: '{dni}'")

    return {
        "total": total,
        "validos": validos,
        "invalidos": invalidos,
        "invalidos_detalle": invalidos_detalle
    }

def mostrar_resumen():
    """Muestra un resumen completo de todas las estadísticas."""
    print("\n========== RESUMEN ESTADÍSTICO ==========\n")
    estadisticas_propiedades()
    estadisticas_pagos()
    estadisticas_contratos()
    estadistica_dominios_email(cargar_inquilinos())
    estadistica_dni_inquilinos(cargar_inquilinos())
    estadistica_pagos_por_inquilino(pagos=cargar_pagos(),
                                    contratos=cargar_contratos(),
                                    inquilinos=cargar_inquilinos(),
                                    norm=norm,
                                    parse_int=parse_int)
    input("Presione Enter para continuar...")