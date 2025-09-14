def modificar_inquilino(matriz):
    id_inquilino = int(input("Ingrese el ID del inquilino a modificar: "))
    for inquilino in matriz:
        if inquilino[0] == id_inquilino:

            nuevo = input("Nuevo nombre: ")
            if nuevo != "":
                inquilino[1] = nuevo

            nuevo = input("Nuevo DNI: ")
            if nuevo != "":
                inquilino[2] = nuevo

            nuevo = input("Nuevo email: ")
            if nuevo != "":
                inquilino[3] = nuevo

            nuevo = input("Nuevo teléfono: ")
            if nuevo != "":
                inquilino[4] = nuevo

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