import json
import os


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

def buscar_propiedades(propiedades, norm, parse_int):
    """
    Reintenta hasta que haya resultados o el usuario presione Enter en vacío.
    - Si se ingresa un ID exacto presente, devuelve [ID].
    - Si no, busca por texto en Dirección / Tipo / Estado / PrecioAlquiler.
    Devuelve: list (vacía si se cancela).
    """
    while True:
        termino = input("Ingrese dirección, tipo, estado, precio o ID (Enter para cancelar): ")
        if termino.strip() == "":
            return []  # cancelación

        t = norm(termino)
        # --- ID exacto: chequear ambas variantes (int y str) ---
        posible_id = parse_int(t)
        if posible_id is not None:
            if posible_id in propiedades:
                return [posible_id]
            pid_str = str(posible_id)
            if pid_str in propiedades:
                return [pid_str]

        # --- Búsqueda por texto ---
        resultados = []
        for pid, p in propiedades.items():
            try:
                direccion = norm(str(p.get("Direccion", "")))
                tipo = norm(str(p.get("Tipo", "")))
                estado = norm(str(p.get("Estado", "")))
                precio = norm(str(p.get("PrecioAlquiler", "")))
                texto = f"{direccion} {tipo} {estado} {precio}"
                if t in texto:
                    resultados.append(pid)  # respetamos el tipo real de la clave
            except (KeyError, AttributeError):
                pass

        if resultados:
            return resultados
        else:
            print("No se encontraron coincidencias. Intente nuevamente.\n")


def seleccionar_propiedad(propiedades, resultados_ids, norm):
    """
    Muestra la lista y permite elegir por ID.
    Reintenta hasta elección válida o Enter vacío (cancela).
    Devuelve: la clave del ID con su tipo original (int o str) o None.
    """
    if not resultados_ids:
        print("No hay resultados para seleccionar.")
        return None

    print("\nResultados encontrados:")
    idx = 0
    total = len(resultados_ids)
    while idx < total:
        pid = resultados_ids[idx]
        try:
            p = propiedades[pid]
            direccion = p.get("Direccion", "")
            tipo = p.get("Tipo", "")
            precio = p.get("PrecioAlquiler", "")
            estado = p.get("Estado", "")
            print(f"ID: {pid} | Dirección: {direccion} | Tipo: {tipo} | Precio: {precio} | Estado: {estado}")
        except (KeyError, AttributeError):
            print(f"ID: {pid} | [Error en lectura de datos de la propiedad]")
        idx += 1

    while True:
        opcion_raw = input("\nSeleccione (número de ID, Enter para cancelar): ")
        if opcion_raw.strip() == "":
            return None  # cancelación
        opcion = norm(opcion_raw)

        # Aceptamos que el usuario escriba número; comparamos por texto
        try:
            id_directo_int = int(opcion)
            id_directo_str = str(id_directo_int)
        except ValueError:
            id_directo_int = None
            id_directo_str = opcion

        k = 0
        while k < len(resultados_ids):
            rid = resultados_ids[k]
            if str(rid) == id_directo_str:
                return rid  # devolvemos el ID con su tipo original
            k += 1

        print("Opción inválida. Intente nuevamente.")