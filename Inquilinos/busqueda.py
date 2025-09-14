
def busqueda_inquilino(matriz):
    while True:  
        termino = input("Ingrese nombre, DNI, email o teléfono del inquilino a buscar: ").lower()
        resultados = [inq for inq in matriz if termino in f"{inq[1]} {inq[2]} {inq[3]} {inq[4]}".lower()]

        if not resultados:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i, inq in enumerate(resultados, start=1):
                print(f"{i} - ID: {inq[0]} | Nombre: {inq[1]} | DNI: {inq[2]} | Email: {inq[3]} | Tel: {inq[4]} | Estado: {inq[5]}")

            opcion = input("\nSeleccione el inquilino (número de la lista o ID): ").lower()
            seleccionado = None

            for i, inq in enumerate(resultados, start=1):
                if opcion == str(i) or opcion == str(inq[0]):
                    print("\nHas seleccionado:")
                    print(f"ID: {inq[0]} | Nombre: {inq[1]} | DNI: {inq[2]} | Email: {inq[3]} | Tel: {inq[4]} | Estado: {inq[5]}")
                    seleccionado = inq
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")
