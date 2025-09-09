def modificar_inquilino(matriz):
    id_inquilino = int(input("Ingrese el ID del inquilino a modificar: "))
    for inquilino in matriz:
        if inquilino[0] == id_inquilino:
            actualizar = lambda i, msg: inquilino.__setitem__(i, nuevo) if (nuevo := input(msg)) else None
            
            actualizar(1, "Nuevo nombre: ")
            actualizar(2, "Nuevo DNI: ")
            actualizar(3, "Nuevo email: ")
            actualizar(4, "Nuevo teléfono: ")

            estado = input("Si desea dar de baja al inquilino ingrese [1] y si desea volver a activarlo [0]: ")
            if estado == "1":
                inquilino[5] = "Inactivo"
            elif estado == "0":
                inquilino[5] = "Activo"
            else:
                print("Opción no válida. El estado no se modificará.")

            print("Inquilino modificado exitosamente.")
            return
    print("Inquilino no encontrado.")
