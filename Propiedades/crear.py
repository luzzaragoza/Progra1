def crear_propiedad(id_propiedad):
    direccion = input("Dirección de la propiedad: ")
    tipo = input("Tipo de propiedad (Departamento: [0] / Casa: [2]): ")
    precio_alquiler = int(input("Precio de alquiler (USD): "))
    estado = "Libre"  # Estado por defecto
    
    return [id_propiedad, direccion, tipo, precio_alquiler, estado]

def crear_matriz_propiedades(cant_propiedades):
    propiedades = []
    for i in range(cant_propiedades):
        id_propiedad = len(propiedades) + 1
        propiedad = crear_propiedad(id_propiedad)
        propiedades.append(propiedad)
    return propiedades
