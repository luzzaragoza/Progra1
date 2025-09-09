def modificar_propiedad(matriz):
    id_propiedad = int(input("Ingrese el ID de la propiedad a modificar: "))
    for propiedad in matriz:
        if propiedad[0] == id_propiedad:
            actualizar = lambda i, msg, cast=str: propiedad.__setitem__(i, cast(nuevo)) if (nuevo := input(msg)) else None

            actualizar(1, "Nueva dirección: ")
            actualizar(2, "Nuevo tipo de propiedad: ")
            actualizar(3, "Nuevo precio de alquiler: ", int)

            estado = input("Si desea dar de baja la propiedad ingrese [1] y si desea volver a activarla [0]: ")
            if estado == "1":
                propiedad[4] = "Ocupada"
            elif estado == "0":
                propiedad[4] = "Libre"
            else:
                print("Opción no válida. El estado no se modificará.")

            print("Propiedad modificada exitosamente.")
            return
    print("Propiedad no encontrada.")
