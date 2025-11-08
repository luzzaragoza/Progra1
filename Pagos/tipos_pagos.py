import os

ARCHIVO_TIPOS = "Pagos/tipos_pagos.txt"

def _asegurar_carpeta():
    carpeta = os.path.dirname(ARCHIVO_TIPOS)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta, exist_ok=True)

# CREA un nuevo tipo de pago y lo guarda en el archivo
def crear_tipo_pago(nombre):
    _asegurar_carpeta()
    nombre = nombre.strip()
    if nombre == "":
        print("Nombre vacío.")
        return

    ultimo = 0
    try:
        with open(ARCHIVO_TIPOS, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                # mantenemos prefijo "P" en lectura
                if len(partes) >= 1 and partes[0].startswith("P"):
                    n = int(partes[0][1:])
                    if n > ultimo:
                        ultimo = n
    except FileNotFoundError:
        pass

    # unificamos prefijo a "P" también en escritura
    codigo = f"P{str(ultimo + 1).zfill(3)}"

    with open(ARCHIVO_TIPOS, "a", encoding="utf-8") as f:
        f.write(f"{codigo};{nombre};1\n")

    print(f"Tipo de pago creado: {codigo} - {nombre}")

# LISTA los tipos activos y deja seleccionar uno (streaming; buffer mínimo)
def seleccionar_tipo_pago():
    activos = []
    try:
        with open(ARCHIVO_TIPOS, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 3:
                    continue
                cod, nom, act = partes
                if act == "1":
                    # guardo SOLO lo necesario para el menú
                    activos.append((cod, nom))
    except FileNotFoundError:
        print("No hay archivo aún.")
        return None

    if not activos:
        print("No hay tipos activos.")
        return None

    print("Tipos de pagos activos:")
    for i, (_, nom) in enumerate(activos, 1):
        print(f"{i}) {nom}")

    op = input("Elegí número o Enter para cancelar: ").strip()
    if op.isdigit():
        n = int(op)
        if 1 <= n <= len(activos):
            cod, nom = activos[n - 1]
            # formato compatible con tu flujo: ["P###", "Nombre", "1"]
            return [cod, nom, "1"]
    print("Cancelado o inválido.")
    return None

# BAJA lógica por código (streaming + temp; una sola pasada)
def baja_logica_tipo_pago(codigo):
    _asegurar_carpeta()
    ruta_tmp = ARCHIVO_TIPOS + ".tmp"
    cambiado = False

    try:
        with open(ARCHIVO_TIPOS, "r", encoding="utf-8") as fin, \
             open(ruta_tmp, "w", encoding="utf-8") as fout:
            for linea in fin:
                linea = linea.strip()
                if not linea:
                    continue
                partes = linea.split(";")
                if len(partes) != 3:
                    # línea rara: la copio tal cual
                    fout.write(linea + "\n")
                    continue

                cod, nom, act = partes
                if cod == codigo and act == "1":
                    act = "0"
                    cambiado = True
                    print(f"Tipo {nom} dado de baja.")
                fout.write(f"{cod};{nom};{act}\n")
    except FileNotFoundError:
        print("No hay archivo aún.")
        return False

    os.replace(ruta_tmp, ARCHIVO_TIPOS)
    return cambiado

# Wrapper: usa el selector y luego da la baja por código
def baja_tipo_pago():
    sel = seleccionar_tipo_pago()   # ["P003", "Transferencia", "1"] o None
    if not sel:
        print("Operación cancelada.")
        return False
    codigo = sel[0]
    return baja_logica_tipo_pago(codigo)

# FUNCIÓN PRINCIPAL (igual a la tuya; solo usa las funciones corregidas)
def tipo_pago(opcion):
    if opcion == "1":
        nuevo = input("Ingrese el tipo de pago nuevo: ").strip()
        crear_tipo_pago(nuevo)
        return nuevo
    elif opcion == "2":
        tipo = seleccionar_tipo_pago()
        if tipo:
            return tipo[1]  # devuelve el nombre
        else:
            return ""
    else:
        print("Opción no válida.")
        return ""

def devuelve_nombre_tipo():
    sel = seleccionar_tipo_pago()
    if not sel:
        print("Operación cancelada.")
        return None
    return sel[1]
