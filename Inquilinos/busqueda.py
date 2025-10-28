def buscar_inquilinos(inquilinos, norm, parse_int):
    """
    Reintenta hasta que haya resultados o el usuario presione Enter en vacío.
    - Si se ingresa un ID exacto presente, devuelve [ID].
    - Si no, busca por texto en Nombre / Telefono / Email / DNI.
    Devuelve: list (vacía si se cancela).
    """
    while True:
        termino = input("Ingrese nombre, teléfono, email, DNI o ID (Enter para cancelar): ")
        if termino.strip() == "":
            return []  # cancelación

        t = norm(termino)

        # --- ID exacto: chequear ambas variantes (int y str) ---
        posible_id = parse_int(t)
        if posible_id is not None:
            # si las claves del dict son int
            if posible_id in inquilinos:
                return [posible_id]
            # si las claves del dict son str (típico al cargar JSON)
            id_str = str(posible_id)
            if id_str in inquilinos:
                return [id_str]

        # --- Búsqueda por texto ---
        resultados = []
        for iid, i in inquilinos.items():
            try:
                nombre = norm(str(i.get("Nombre", "")))
                tel    = norm(str(i.get("Telefono", "")))
                email  = norm(str(i.get("Email", "")))
                dni    = norm(str(i.get("DNI", "")))
                texto  = f"{nombre} {tel} {email} {dni}"
                if t in texto:
                    resultados.append(iid)  # respetamos el TIPO real de la clave
            except (KeyError, AttributeError):
                pass

        if resultados:
            return resultados
        else:
            print("No se encontraron coincidencias. Intente nuevamente.\n")


def seleccionar_inquilino(inquilinos, resultados_ids, norm):
    """
    Muestra la lista y permite elegir por ID.
    Reintenta hasta elección válida o Enter vacío (cancela).
    Devuelve: la clave del ID con su TIPO original (int o str) o None.
    """
    print("\nResultados encontrados:")
    idx = 0
    total = len(resultados_ids)
    while idx < total:
        iid = resultados_ids[idx]
        try:
            i = inquilinos[iid]
            nombre = i.get("Nombre", "")
            tel = i.get("Telefono", "")
            email = i.get("Email", "")
            print(f"ID: {iid} | Nombre: {nombre} | Teléfono: {tel} | Email: {email}")
        except (KeyError, AttributeError):
            print(f"ID: {iid} | [Error en lectura de datos del inquilino]")
        idx += 1

    while True:
        opcion_raw = input("\nSeleccione (número de ID, Enter para cancelar): ")
        if opcion_raw.strip() == "":
            return None  # cancelación
        opcion = norm(opcion_raw)

        # Aceptamos que el usuario escriba número; comparamos por TEXTO
        try:
            id_directo_int = int(opcion)
            id_directo_str = str(id_directo_int)
        except ValueError:
            # también permitir IDs no numéricos (poco común, pero seguro)
            id_directo_int = None
            id_directo_str = opcion

        # Buscar en resultados por comparación textual
        k = 0
        while k < len(resultados_ids):
            rid = resultados_ids[k]
            if str(rid) == id_directo_str:
                return rid  # devolvemos el ID con su tipo original
            k += 1

        print("Opción inválida. Intente nuevamente.")
