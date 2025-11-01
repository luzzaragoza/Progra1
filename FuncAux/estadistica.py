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
    
    if len(pagos) == 0:
        print("\nNo hay pagos registrados.")
        return
    
    efectivo = 0
    tarjeta = 0
    transferencia = 0
    
    for id_pago in pagos:
        pago = pagos[id_pago]
        metodo = pago['Método']
        
        if metodo == 'Efectivo':
            efectivo = efectivo + 1
        elif metodo == 'Tarjeta' or metodo == 'Débito':
            tarjeta = tarjeta + 1
        elif metodo == 'Transferencia':
            transferencia = transferencia + 1
    
    print("\n----- Estadísticas de Pagos -----")
    print("Pagos en efectivo:", efectivo)
    print("Pagos con tarjeta:", tarjeta)
    print("Pagos por transferencia:", transferencia)
    print()

def estadisticas_contratos():
    """Muestra estadísticas de contratos."""
    contratos = cargar_contratos()
    
    if len(contratos) == 0:
        print("\nNo hay contratos registrados.")
        return
    
    vigentes = 0
    finalizados = 0
    
    for id_contrato in contratos:
        contrato = contratos[id_contrato]
        
        if contrato['Estado'] == 'Vigente':
            vigentes = vigentes + 1
        elif contrato['Estado'] == 'Finalizado':
            finalizados = finalizados + 1
    
    print("\n----- Estadísticas de Contratos -----")
    print("Contratos vigentes:", vigentes)
    print("Contratos dados de baja:", finalizados)
    print()

def mostrar_resumen():
    """Muestra un resumen completo de todas las estadísticas."""
    print("\n========== RESUMEN ESTADÍSTICO ==========\n")
    estadisticas_propiedades()
    estadisticas_pagos()
    estadisticas_contratos()
    input("Presione Enter para continuar...")
