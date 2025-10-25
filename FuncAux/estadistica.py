# FuncAux/estadisticas.py

# --- IMPORTS ---
from Inquilinos.datos import inquilinos
from Propiedades.datos import propiedades
from Contratos.datos import contratos
from Pagos.datos import pagos

#en estadística debe haber: cantidad de inmuebles, cuantos ocupados y cuantos libres, sin opción de compra ya que es solo para alquileres; hacer una estadística para pagos aobre cuantos pagan en efvo, cuantos en tarjeta y cuantos en trasnferencia; contratos vigentes, dados de baja; cantidad de casas y cantidad de departamentos; 
# --- FUNCIONES AUXILIARES ---
def calcular_ocupacion(propiedades):
    total = len(propiedades)
    ocupados = 0

    for propiedad in propiedades:
        if propiedad.get("estado", "").lower() == "ocupado":
            ocupados += 1

    libres = total - ocupados
    return {"total": total, "ocupados": ocupados, "libres": libres}


def contar_inquilinos(inquilinos):
    total = len(inquilinos)
    compradores = 0
    alquiladores = 0

    for i in inquilinos:
        tipo = i.get("tipo", "").lower()
        if tipo == "compra":
            compradores += 1
        elif tipo == "alquiler":
            alquiladores += 1

    return {"total": total, "compraron": compradores, "alquilaron": alquiladores}


def contar_contratos(contratos):
    total = len(contratos)
    activos = 0
    finalizados = 0

    for c in contratos:
        estado = c.get("estado", "").lower()
        if estado == "activo":
            activos += 1
        elif estado == "finalizado":
            finalizados += 1

    return {"total": total, "activos": activos, "finalizados": finalizados}


# --- FUNCIÓN PRINCIPAL ---
def mostrar_resumen():
    print("=== RESUMEN ESTADÍSTICO ===\n")

    # Ocupación de propiedades
    ocupacion = calcular_ocupacion(propiedades)
    print("PROPIEDADES:")
    print(f"  Total: {ocupacion['total']}")
    print(f"  Ocupadas: {ocupacion['ocupados']}")
    print(f"  Libres: {ocupacion['libres']}\n")

    # Inquilinos
    inq = contar_inquilinos(inquilinos)
    print("INQUILINOS:")
    print(f"  Total: {inq['total']}")
    print(f"  Compraron: {inq['compraron']}")
    print(f"  Alquilaron: {inq['alquilaron']}\n")

    # Contratos
    cont = contar_contratos(contratos)
    print("CONTRATOS:")
    print(f"  Total: {cont['total']}")
    print(f"  Activos: {cont['activos']}")
    print(f"  Finalizados: {cont['finalizados']}\n")

    print("============================\n")

