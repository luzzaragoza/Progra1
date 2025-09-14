def modificar_inquilino(matriz):
    id_inquilino = int(input("Ingrese el ID del inquilino a modificar: "))
    for inquilino in matriz:
        if inquilino[0] == id_inquilino:

            nuevo = input("Nuevo nombre (Enter para no modificar): ")
            if nuevo != "":
                inquilino[1] = nuevo

            nuevo = input("Nuevo DNI (Enter para no modificar): ")
            if nuevo != "":
                inquilino[2] = int(nuevo)  # solo convierte si no está vacío

            nuevo = input("Nuevo email (Enter para no modificar): ")
            if nuevo != "":
                inquilino[3] = nuevo

            nuevo = input("Nuevo teléfono (Enter para no modificar): ")
            if nuevo != "":
                inquilino[4] = int(nuevo)  # solo convierte si no está vacío

            estado = input("Si desea dar de baja al inquilino ingrese [1], para activarlo [0], o Enter para no modificar: ")
            if estado == "1":
                inquilino[5] = "Inactivo"
            elif estado == "0":
                inquilino[5] = "Activo"
            elif estado.strip() == "":
                pass  # no se modifica
            else:
                print("Opción no válida. El estado no se modificará.")

            print("Inquilino modificado exitosamente.")
            return
    print("Inquilino no encontrado.")
