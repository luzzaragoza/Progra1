def crear_propiedad(id_propiedad):
    direccion = input("Dirección de la propiedad: ")
    
    while True:
        opcion_tipo = input("Tipo de propiedad (Casa [0] / Departamento [1]): ")
        if opcion_tipo == "0":
            tipo = "Casa"
            break
        elif opcion_tipo == "1":
            tipo = "Departamento"
            break
        else:
            print("Opción no válida, vuelva a intentar.")
    
    precio_alquiler = int(input("Precio de alquiler (USD): "))
    estado = "Libre" 
    
    return [id_propiedad, direccion, tipo, precio_alquiler, estado]


def crear_matriz_propiedades(cant_propiedades):
    propiedades = []
    for i in range(cant_propiedades):
        id_propiedad = len(propiedades) + 1
        propiedad = crear_propiedad(id_propiedad)
        propiedades.append(propiedad)
    return propiedades


'''def crear_propiedad(id_propiedad):
    direccion = input("Dirección de la propiedad: ")
    ciudad = input("Ciudad: ")
    valor = float(input("Valor del alquiler: "))
    estado = "Disponible"
    return [id_propiedad, direccion, ciudad, valor, estado]


def crear_matriz_propiedades(cant_propiedades, propiedades=None):
    if propiedades is None:
        propiedades = []
    for _ in range(cant_propiedades):
        id_propiedad = generar_id(propiedades)
        propiedad = crear_propiedad(id_propiedad)
        propiedades.append(propiedad)
    return propiedades


def imprimir_propiedades(propiedades):
    print("{:<4} {:<30} {:<15} {:<10} {:<12}".format("ID","DIRECCIÓN","CIUDAD","ALQ","ESTADO"))
    for p in propiedades:
        print("{:<4} {:<30} {:<15} {:<10} {:<12}".format(p[0], p[1], p[2], p[3], p[4]))
'''