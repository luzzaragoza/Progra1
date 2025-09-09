def busqueda_propiedad(matriz):
    while True:  # Bucle para reintentos
        termino = input("Ingrese dirección o tipo de propiedad a buscar: ").lower()
        resultados = [prop for prop in matriz if termino in f"{prop[1]} {prop[2]}".lower()]

        if not resultados:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i, prop in enumerate(resultados, start=1):
                print(f"{i} - ID: {prop[0]} | Dirección: {prop[1]} | Tipo: {prop[2]} | Precio: {prop[3]} | Estado: {prop[4]}")

            opcion = input("\nSeleccione la propiedad (número de la lista o ID): ").lower()
            seleccionado = None

            for i, prop in enumerate(resultados, start=1):
                if opcion == str(i) or opcion == str(prop[0]):
                    print("\nHas seleccionado:")
                    print(f"ID: {prop[0]} | Dirección: {prop[1]} | Tipo: {prop[2]} | Precio: {prop[3]} | Estado: {prop[4]}")
                    seleccionado = prop
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")
