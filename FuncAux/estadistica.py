import json
import os

def cargar_propiedades():
    """Carga las propiedades desde el archivo JSON."""
    ruta = os.path.join('Propiedades', 'datos.json')
    if not os.path.exists(ruta):
        return {}
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

def cargar_contratos():
    """Carga los contratos desde el archivo JSON."""
    ruta = os.path.join('Contratos', 'datos.json')
    if not os.path.exists(ruta):
        return {}
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

def cargar_pagos():
    """Carga los pagos desde el archivo JSON."""
    ruta = os.path.join('Pagos', 'datos.json')
    if not os.path.exists(ruta):
        return {}
    try:
        with open(ruta, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except:
        return {}

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
    
    print("\n----- Estadísticas de Propiedades -----")
    print("Total de inmuebles:", total)
    print("Inmuebles ocupados:", ocupados)
    print("Inmuebles libres:", libres)
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

    print("\n----- Estadísticas de Contratos -----")
    print("Contratos vigentes:", vigentes)
    print("Contratos dados de baja:", finalizados)
    print()

from functools import reduce

def total_por_metodo(metodo):
    """Devuelve el total de montos de pagos según el método indicado."""
    pagos = cargar_pagos()
    if not pagos:
        print("\nNo hay pagos registrados.")
        return 0

    # valores del diccionario (sin IDs)
    valores = pagos.values()

    # filtramos solo los del método indicado
    filtrados = filter(lambda p: p["Método"] == metodo, valores)

    # convertimos montos a float por si vinieran como str
    montos = map(lambda p: float(p["Monto"]), filtrados)

    # acumulamos la suma total
    total = reduce(lambda acc, m: acc + m, montos, 0)

    print(f"💰 Total en {metodo}: ${total:,.2f}")
    return total


def mostrar_resumen():
    """Muestra un resumen completo de todas las estadísticas."""
    print("\n========== RESUMEN ESTADÍSTICO ==========\n")
    estadisticas_propiedades()
    estadisticas_pagos()
    estadisticas_contratos()
    input("Presione Enter para continuar...")
