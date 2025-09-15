

def calcular_ocupacion(inmuebles):
    # inmuebles: [ID, Dirección, Ciudad/Tipo, Precio, Estado]
    total = len(inmuebles)
    ocupados = 0
    i = 0
    while i < total:
        fila = inmuebles[i]
        if len(fila) >= 5:
            estado = str(fila[4]).lower()
            if estado.startswith("ocup"):  # "ocupado/ocupada"
                ocupados = ocupados + 1
        i = i + 1
    libres = total - ocupados

    if total > 0:
        porc_oc = ocupados / total * 100
        porc_li = libres / total * 100
    else:
        porc_oc = 0
        porc_li = 0

    return {
        "total": total,
        "ocupados": ocupados,
        "libres": libres,
        "porc_ocupados": porc_oc,
        "porc_libres": porc_li,
    }


def ingreso_mensual(contratos):
    """
    Soporta:
    A) [id, id_inq, id_prop, mes, monto]
    B) [id, id_prop, id_inq, fecha_ini, fecha_fin, monto]
    Agrupa por "mes" usando slicing simple si viene 'YYYY-MM-...'.
    """
    ingresos = {}  # dict permitido
    i = 0
    while i < len(contratos):
        c = contratos[i]
        if len(c) >= 6:
            mes_raw = str(c[3])
            s = mes_raw
            if len(s) >= 7 and len(s) > 4 and s[4] == "-":
                mes = s[:7]    # "YYYY-MM"
            else:
                mes = s
            monto_raw = str(c[5])
            monto_s = monto_raw.replace(".", "")
            monto_s = monto_s.replace(",", ".")
            try:
                monto = float(monto_s)
            except Exception:
                monto = 0.0
        elif len(c) >= 5:
            mes_raw = str(c[3])
            s = mes_raw
            if len(s) >= 7 and len(s) > 4 and s[4] == "-":
                mes = s[:7]
            else:
                mes = s
            monto_raw = str(c[4])
            monto_s = monto_raw.replace(".", "")
            monto_s = monto_s.replace(",", ".")
            try:
                monto = float(monto_s)
            except Exception:
                monto = 0.0
        else:
            i = i + 1
            continue

        if mes in ingresos:
            ingresos[mes] = ingresos[mes] + monto
        else:
            ingresos[mes] = monto

        i = i + 1

    # ordenar por clave (mes) sin lambda
    claves = list(ingresos.keys())
    claves.sort()
    ordenado = {}
    j = 0
    while j < len(claves):
        k = claves[j]
        ordenado[k] = ingresos[k]
        j = j + 1

    return ordenado


def valores_inmuebles(inmuebles):
    valores = []
    i = 0
    while i < len(inmuebles):
        fila = inmuebles[i]
        if len(fila) >= 4:
            v_raw = str(fila[3])
            v_s = v_raw.replace(".", "")
            v_s = v_s.replace(",", ".")
            try:
                v = float(v_s)
                valores.append(v)
            except Exception:
                # ignora valores no numéricos
                pass
        i = i + 1

    if len(valores) == 0:
        return {"max": None, "min": None}

    # max/min permitidos
    return {"max": max(valores), "min": min(valores)}


def mostrar_ocupacion(inmuebles):
    r = calcular_ocupacion(inmuebles)
    print("ESTADO DE INMUEBLES")
    print("Total: " + str(r["total"]))
    print("Ocupados: " + str(r["ocupados"]) + " (" + ("%.2f" % r["porc_ocupados"]) + "%)")
    print("Libres: " + str(r["libres"]) + " (" + ("%.2f" % r["porc_libres"]) + "%)")


def mostrar_ingresos(contratos):
    ingresos = ingreso_mensual(contratos)
    print("\nINGRESOS POR MES")
    if len(ingresos) == 0:
        print("Sin datos.")
        return

    # recorrer items en orden
    claves = list(ingresos.keys())
    claves.sort()
    i = 0
    while i < len(claves):
        mes = claves[i]
        monto = ingresos[mes]
        # formateo miles "a mano" sin helpers
        entero = int(round(monto))
        s = str(entero)
        negativo = False
        if entero < 0:
            negativo = True
            s = str(-entero)
        partes = []
        while len(s) > 3:
            partes.insert(0, s[-3:])
            s = s[:-3]
        partes.insert(0, s)
        miles = ".".join(partes)
        if negativo:
            miles = "-" + miles
        print(mes + ": $" + miles)
        i = i + 1


def mostrar_valores(inmuebles):
    v = valores_inmuebles(inmuebles)
    print("\nVALORES DE INMUEBLES")
    if v["max"] is None:
        print("Más alto: -")
        print("Más bajo: -")
        return

    # formateo miles para max
    entero_max = int(round(v["max"]))
    s = str(entero_max)
    neg = False
    if entero_max < 0:
        neg = True
        s = str(-entero_max)
    partes = []
    while len(s) > 3:
        partes.insert(0, s[-3:])
        s = s[:-3]
    partes.insert(0, s)
    miles_max = ".".join(partes)
    if neg:
        miles_max = "-" + miles_max

    # formateo miles para min
    entero_min = int(round(v["min"]))
    s2 = str(entero_min)
    neg2 = False
    if entero_min < 0:
        neg2 = True
        s2 = str(-entero_min)
    partes2 = []
    while len(s2) > 3:
        partes2.insert(0, s2[-3:])
        s2 = s2[:-3]
    partes2.insert(0, s2)
    miles_min = ".".join(partes2)
    if neg2:
        miles_min = "-" + miles_min

    print("Más alto: $" + miles_max)
    print("Más bajo: $" + miles_min)


def mostrar_resumen(inmuebles, contratos):
    print("\n========= RESUMEN ESTADÍSTICO =========")
    mostrar_ocupacion(inmuebles)
    mostrar_ingresos(contratos)
    mostrar_valores(inmuebles)
    print("=======================================")