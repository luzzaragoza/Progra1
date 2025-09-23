from Propiedades.datos import propiedades  

def modificar_propiedad():
    print("----- Modificar Propiedad -----")
    id_prop = int(input("Ingrese el ID de la propiedad a modificar: "))

    if id_prop not in propiedades:
        print("❌ Propiedad no encontrada.\n")
        return False

    p = propiedades[id_prop]

    # Dirección
    print(f"\nDirección actual: {p['Direccion']}")
    nueva_direccion = input("Nueva dirección (Enter para dejar igual): ").strip()
    if nueva_direccion != "":
        p["Direccion"] = nueva_direccion
    elif nueva_direccion == "":
        pass

    # Tipo (solo Casa / Departamento, como tu versión original)
    print(f"Tipo actual: {p['Tipo']}")
    nuevo_tipo = input("Nuevo tipo (Casa [0] / Departamento [1] / Otro [2] / Enter para dejar igual): ").strip()
    if nuevo_tipo == "0":
        p["Tipo"] = "Casa"
    elif nuevo_tipo == "1":
        p["Tipo"] = "Departamento"
    elif nuevo_tipo == "2":
        otro_tipo = input("Ingrese el tipo de propiedad: ").strip()
        if otro_tipo != "":
            p["Tipo"] = otro_tipo
    elif nuevo_tipo == "":
        pass

    # Precio de alquiler
    print(f"Precio actual: ${p['PrecioAlquiler']}")
    nuevo_precio = input("Nuevo precio de alquiler (Enter para dejar igual): ").strip()
    if nuevo_precio != "" and nuevo_precio.isdigit():
        p["PrecioAlquiler"] = nuevo_precio
    elif nuevo_precio == "":
        pass

    print("\n✅ Propiedad modificada exitosamente.\n")
    return True