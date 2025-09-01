def busqueda_inquilino(matriz):
    while True:  # Bucle para reintentos
        termino = input("Ingrese nombre o apellido a buscar: ").lower()
        resultados = []

        for i in range(1, len(matriz)):  # asume que la matriz tiene encabezado
            nombre_completo = matriz[i][1].lower()
            if termino in nombre_completo:
                resultados.append(matriz[i])

        if len(resultados) == 0:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i in range(len(resultados)):
                letra = chr(97 + i)
                inquilino = resultados[i]
                print(letra, "-", inquilino[1], "| DNI:", inquilino[2], "| Email:", inquilino[3], "| Tel:", inquilino[4])

            opcion = input("\nSeleccione el inquilino (a, b, c...): ").lower()
            seleccionado = None
            for i in range(len(resultados)):
                letra = chr(97 + i)
                if opcion == letra:
                    inquilino = resultados[i]
                    print("\nHas seleccionado:")
                    print("ID:", inquilino[0], "| Nombre:", inquilino[1], "| DNI:", inquilino[2], "| Email:", inquilino[3], "| Tel:", inquilino[4])
                    seleccionado = inquilino
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")
