ARCHIVO_TIPOS = "Propiedades/tipos_propiedad.txt"

# CREA un nuevo tipo de propiedad y lo guarda en el archivo
def crear_tipo_propiedad(nombre):
    nombre = nombre.strip()
    if nombre == "":
        print("Nombre vacío.")
        return

    ultimo = 0
    try:
        with open(ARCHIVO_TIPOS, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split(";")
                if len(partes) >= 1 and partes[0].startswith("P"):
                    n = int(partes[0][1:])
                    if n > ultimo:
                        ultimo = n
    except FileNotFoundError:
        pass

    codigo = f"P{str(ultimo + 1).zfill(3)}"

    with open(ARCHIVO_TIPOS, "a", encoding="utf-8") as f:
        f.write(f"{codigo};{nombre};1\n")

    print(f"Tipo de propiedad creado: {codigo} - {nombre}")


# LISTA los tipos activos y deja seleccionar uno
def seleccionar_tipo_propiedad():
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

    print("Tipos de propiedad activos:")
    for i, (_, nom) in enumerate(activos, 1):
        print(f"{i}) {nom}")

    op = input("Elegí número o Enter para cancelar: ")
    if op.isdigit():
        n = int(op)
        if 1 <= n <= len(activos):
            cod, nom = activos[n - 1]
            # Devuelvo con el mismo formato que usabas: ["P###", "Nombre", "1"]
            return [cod, nom, "1"]

    print("Cancelado o inválido.")
    return None


def seleccionar_baja_tipo(codigo):
    import os
    ruta_tmp = ARCHIVO_TIPOS + ".tmp"
    encontrado = False

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
                    encontrado = True
                    print(f"Tipo {codigo} dado de baja.")
                fout.write(f"{cod};{nom};{act}\n")
    except FileNotFoundError:
        print("No hay archivo aún.")
        return False

    # Reemplazo atómico
    os.replace(ruta_tmp, ARCHIVO_TIPOS)
    return encontrado


def baja_tipo_propiedad():
    sel = seleccionar_tipo_propiedad()   # ["P003", "Duplex", "1"] o None
    if not sel:
        print("Operación cancelada.")
        return False
    codigo = sel[0]
    return seleccionar_baja_tipo(codigo)


# FUNCIÓN PRINCIPAL (versión adaptada de la tuya)
def tipo_propiedad(opcion):
    if opcion == "1":
        nuevo = input("Ingrese el tipo de propiedad nuevo: ").strip()
        crear_tipo_propiedad(nuevo)
        return nuevo
    elif opcion == "2":
        tipo = seleccionar_tipo_propiedad()
        if tipo:
            return tipo[1]  # devuelve el nombre
        else:
            return ""
    else:
        print("Opción no válida.")
        return ""
