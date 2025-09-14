def modificar_propiedad(matriz):
    id_propiedad = int(input("Ingrese el ID de la propiedad a modificar: "))
    
    for propiedad in matriz:
        if propiedad[0] == id_propiedad:
            # Dirección
            print(f"Dirección actual: {propiedad[1]}")
            nuevo = input("Nueva dirección (Enter para dejar igual): ")
            if nuevo != "":
                propiedad[1] = nuevo

            print(f"Tipo actual: {propiedad[2]}")
            while True:
                nuevo = input("Nuevo tipo de propiedad (Casa [0] / Departamento [1] / Enter para dejar igual): ")
                if nuevo == "0":
                    propiedad[2] = "Casa"
                    break
                elif nuevo == "1":
                    propiedad[2] = "Departamento"
                    break
                elif nuevo == "":
                    break  
                else:
                    print("Opción no válida. Vuelva a intentar.")

            print(f"Precio actual: {propiedad[3]}")
            nuevo = input("Nuevo precio de alquiler (Enter para dejar igual): ")
            if nuevo != "":
                propiedad[3] = int(nuevo)

            print(f"Estado actual: {propiedad[4]}")
            while True:
                estado = input("Dar de baja [1], activar [0], Enter para no cambiar: ")
                if estado == "1":
                    propiedad[4] = "Ocupada"
                    break
                elif estado == "0":
                    propiedad[4] = "Libre"
                    break
                elif estado == "":
                    break  
                else:
                    print("Opción inválida. Vuelva a intentar.")

            print("\n✅ Propiedad modificada exitosamente.")
            return
    
    print("❌ Propiedad no encontrada.")
