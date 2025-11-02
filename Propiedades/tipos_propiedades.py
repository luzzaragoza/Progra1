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
    try:
        with open(ARCHIVO_TIPOS, "r", encoding="utf-8") as f:
            tipos = [l.strip().split(";") for l in f if l.strip()]
    except FileNotFoundError:
        print("No hay archivo aún.")
        return None

    activos = [t for t in tipos if len(t) == 3 and t[2] == "1"]
    if not activos:
        print("No hay tipos activos.")
        return None

    print("Tipos de propiedad activos:")
    for i, t in enumerate(activos, 1):
        print(f"{i}) {t[1]}")

    op = input("Elegí número o Enter para cancelar: ")
    if op.isdigit():
        n = int(op)
        if 1 <= n <= len(activos):
            return activos[n - 1]
    print("Cancelado o inválido.")
    return None

# BAJA lógica de un tipo (marca con 0)
def seleccionar_baja_tipo(codigo):
    try:
        with open(ARCHIVO_TIPOS, "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print("No hay archivo aún.")
        return

    with open(ARCHIVO_TIPOS, "w", encoding="utf-8") as f:
        for linea in lineas:
            partes = linea.strip().split(";")
            if partes[0] == codigo:
                partes[2] = "0"
                print(f"Tipo {codigo} dado de baja.")
            f.write(";".join(partes) + "\n")

def baja_tipo_propiedad():
    sel = seleccionar_tipo_propiedad()   # devuelve algo como ["P003", "Duplex", "1"] o None
    if not sel:
        print("Operación cancelada.")
        return False
    codigo = sel[0]  # el ID está en la primera posición
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
