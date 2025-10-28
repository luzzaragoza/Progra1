

def buscar_contratos(contratos, norm, parse_int):
    """
    Reintenta hasta que haya resultados o el usuario presione Enter en vacío.
    - Si se ingresa un ID de contrato exacto presente, devuelve [ID] (con el TIPO real de la clave).
    - Si no, busca por texto en Fecha_Inicio / Fecha_Fin / Estado / Monto (como texto).
    Devuelve: list (vacía si se cancela).
    """
    while True:
        termino = input("Ingrese fecha (YYYY-MM-DD), estado, monto o ID de contrato (Enter para cancelar): ")
        if termino.strip() == "":
            return []  # cancelación

        t = norm(termino)

        # --- ID exacto: chequear variantes int/str ---
        posible_id = parse_int(t)
        if posible_id is not None:
            if posible_id in contratos:          # claves int
                return [posible_id]
            cid_str = str(posible_id)            # claves str (JSON)
            if cid_str in contratos:
                return [cid_str]

        # --- Búsqueda por texto (sin ID_Inquilino ni ID_Propiedad) ---
        resultados = []
        for cid, c in contratos.items():
            try:
                inicio = norm(str(c.get("Fecha_Inicio", "")))
                fin    = norm(str(c.get("Fecha_Fin", "")))
                estado = norm(str(c.get("Estado", "")))
                monto  = norm(str(c.get("Monto", "")))   # como texto para permitir búsqueda libre
                texto  = f"{inicio} {fin} {estado} {monto}"
                if t in texto:
                    resultados.append(cid)  # respetamos el TIPO real de la clave
            except (KeyError, AttributeError):
                pass

        if resultados:
            return resultados
        else:
            print("No se encontraron coincidencias. Intente nuevamente.\n")


def seleccionar_contrato(contratos, resultados_ids, norm):
    """
    Muestra la lista y permite elegir por ID de contrato.
    Reintenta hasta elección válida o Enter vacío (cancela).
    Devuelve: la clave del ID con su TIPO original (int o str) o None.
    """
    if not resultados_ids:
        print("No hay resultados para seleccionar.")
        return None

    print("\nResultados encontrados:")
    idx = 0
    total = len(resultados_ids)
    while idx < total:
        cid = resultados_ids[idx]
        try:
            c = contratos[cid]
            inicio = c.get("Fecha_Inicio", "")
            fin    = c.get("Fecha_Fin", "")
            estado = c.get("Estado", "")
            monto  = c.get("Monto", "")
            print(f"ID: {cid} | Inicio: {inicio} | Fin: {fin} | Monto: {monto} | Estado: {estado}")
        except (KeyError, AttributeError):
            print(f"ID: {cid} | [Error en lectura de datos del contrato]")
        idx += 1

    while True:
        opcion_raw = input("\nSeleccione (número de ID de contrato, Enter para cancelar): ")
        if opcion_raw.strip() == "":
            return None  # cancelación
        opcion = norm(opcion_raw)

        # Aceptamos que escriban número; comparamos en texto
        try:
            id_directo_int = int(opcion)
            id_directo_str = str(id_directo_int)
        except ValueError:
            id_directo_int = None
            id_directo_str = opcion  # por si algún ID no fuera numérico

        k = 0
        while k < len(resultados_ids):
            rid = resultados_ids[k]
            if str(rid) == id_directo_str:
                return rid  # devolvemos el ID con su tipo original
            k += 1

        print("Opción inválida. Intente nuevamente.")
