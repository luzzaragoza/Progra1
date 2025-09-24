from Propiedades.datos import propiedades
from FuncAux.validaciones import norm, nonempty, parse_int
from Propiedades.crear import tipo_propiedad

def modificar_propiedad():
    print("----- Modificar Propiedad -----")
    raw_id = input("Ingrese el ID de la propiedad a modificar: ")
    id_prop = parse_int(norm(raw_id))
    if id_prop is None:
        print("ID inválido. Debe ser numérico.\n")
        return False

    if id_prop not in propiedades:
        print("❌ Propiedad no encontrada.\n")
        return False

    p = propiedades[id_prop]

    # Dirección
    print(f"\nDirección actual: {p['Direccion']}")
    nueva_direccion = input("Nueva dirección (Enter para dejar igual): ")
    if nonempty(nueva_direccion):
        p["Direccion"] = norm(nueva_direccion)

    # Tipo (0/1/2) con Enter para mantener
    print(f"Tipo actual: {p['Tipo']}")
    op = tipo_propiedad(input("Nuevo tipo (0 - Casa, 1 - Departamento, 2 - Otro, Enter para dejar igual): ").strip())
    if op == "Casa" or op == "Departamento":
        p["Tipo"] = op
    elif nonempty(op):
        p["Tipo"] = op
    # Si op está vacío, se mantiene el tipo actual

    # Precio de alquiler
    print(f"Precio actual: ${p['PrecioAlquiler']}")
    raw_precio = input("Nuevo precio de alquiler (Enter para dejar igual): ")
    raw_precio = norm(raw_precio)
    if nonempty(raw_precio):
        nuevo_precio = parse_int(raw_precio)
        if nuevo_precio is not None and nuevo_precio > 0:
            p["PrecioAlquiler"] = nuevo_precio
        else:
            print("Ingrese un entero positivo. Se mantiene el precio actual.")

    print("\n✅ Propiedad modificada exitosamente.\n")
    return True
