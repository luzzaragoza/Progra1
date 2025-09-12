# estadisticas.py

def calcular_ocupacion(inmuebles):
    total = len(inmuebles)
    ocupados = sum(1 for i in inmuebles if i.get("estado") == "ocupado")
    libres = total - ocupados

    return {
        "total": total,
        "ocupados": ocupados,
        "libres": libres,
        "porc_ocupados": (ocupados / total * 100) if total > 0 else 0,
        "porc_libres": (libres / total * 100) if total > 0 else 0,
    }


def ingreso_mensual(contratos):
    ingresos = {}
    for c in contratos:
        mes = c.get("mes")
        monto = c.get("monto", 0)
        ingresos[mes] = ingresos.get(mes, 0) + monto
    return ingresos


def valores_inmuebles(inmuebles):
    if not inmuebles:
        return {"max": None, "min": None}

    valores = [i.get("valor", 0) for i in inmuebles]
    return {"max": max(valores), "min": min(valores)}


def resumen_estadistico(inmuebles, contratos):
    return {
        "ocupacion": calcular_ocupacion(inmuebles),
        "ingresos": ingreso_mensual(contratos),
        "valores": valores_inmuebles(inmuebles),
    }




def mostrar_ocupacion(inmuebles):
    stats = calcular_ocupacion(inmuebles)
    print("ESTADO DE INMUEBLES")
    print(f"Total: {stats['total']}")
    print(f"Ocupados: {stats['ocupados']} ({stats['porc_ocupados']:.2f}%)")
    print(f"Libres: {stats['libres']} ({stats['porc_libres']:.2f}%)")


def mostrar_ingresos(contratos):
    ingresos = ingreso_mensual(contratos)
    print("\n💰 INGRESOS POR MES")
    for mes, monto in ingresos.items():
        print(f"{mes}: ${monto}")


def mostrar_valores(inmuebles):
    valores = valores_inmuebles(inmuebles)
    print("\n🏠 VALORES DE INMUEBLES")
    print(f"Más alto: ${valores['max']}")
    print(f"Más bajo: ${valores['min']}")


def mostrar_resumen(inmuebles, contratos):
    print("\n========= RESUMEN ESTADÍSTICO =========")
    mostrar_ocupacion(inmuebles)
    mostrar_ingresos(contratos)
    mostrar_valores(inmuebles)
    print("==========================================")
