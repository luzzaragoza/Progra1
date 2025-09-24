from Propiedades.datos import propiedades
from FuncAux.validaciones import norm, nonempty, parse_int

def tipo_propiedad(opcion):
    tipo = ""
    if opcion == "0":
        tipo = "Casa"
    elif opcion == "1":
        tipo = "Departamento"
    elif opcion == "2":
        tipo = input("Ingrese el tipo de propiedad: ").strip()
    else:
        print("Opción no válida, vuelva a intentar.")
    
    return tipo

def crear_propiedad(id_propiedad):
    direccion = input("Dirección de la propiedad (Calle y número): ").strip()
    while not nonempty(direccion):
        print("La dirección no puede estar vacía. Intente nuevamente.")
        direccion = input("Dirección de la propiedad (Calle y número): ").strip()
    
    print("Seleccione el tipo de propiedad:")
    print("0 - Casa")
    print("1 - Departamento")
    print("2 - Otro")
    opcion = input("Opción: ").strip()
    tipo = tipo_propiedad(opcion)
    
    
    precio_alquiler = int(input("Precio de alquiler (USD): "))
    while precio_alquiler <= 0:
        print("El precio de alquiler debe ser un número positivo. Intente nuevamente.")
        precio_alquiler = int(input("Precio de alquiler (USD): "))

    propiedades[id_propiedad] = {f"Direccion": direccion, "Tipo": tipo, "PrecioAlquiler": precio_alquiler, "Estado": "Disponible"}
    print(f"Propiedad con ID {id_propiedad} creada exitosamente.\n")
    
    return propiedades


def crear_cant_propiedades(cant_propiedades):
    creados = []
    for i in range(cant_propiedades):
        print(f"--- Ingresando datos de la propiedad {i + 1} ---")
        id_propiedad = len(propiedades) + 1
        nuevo = crear_propiedad(id_propiedad)
        creados.append(nuevo)
    print(f"Propiedades creadas exitosamente: ({len(creados)}) \n")
    return creados