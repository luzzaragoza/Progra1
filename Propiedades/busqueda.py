def busqueda_propiedad(matriz):
    while True:  # Bucle para reintentos
        termino = input("Ingrese dirección o tipo de propiedad a buscar: ").lower()
        resultados = []

        for i in range(len(matriz)):
            direccion_tipo = f"{matriz[i][1]} {matriz[i][2]}".lower()
            if termino in direccion_tipo:
                resultados.append(matriz[i])

        if len(resultados) == 0:
            print("No se encontraron coincidencias. Intente nuevamente.\n")
        else:
            print("\nResultados encontrados:")
            for i in range(len(resultados)):
                letra = chr(97 + i) if i < 26 else str(i + 1)
                prop = resultados[i]
                print(f"{letra} - Dirección: {prop[1]} | Tipo: {prop[2]} | Precio: {prop[3]} | Estado: {prop[4]}")

            opcion = input("\nSeleccione la propiedad (letra o número): ").lower()
            seleccionado = None
            for i in range(len(resultados)):
                letra = chr(97 + i) if i < 26 else str(i + 1)
                if opcion == letra:
                    prop = resultados[i]
                    print("\nHas seleccionado:")
                    print(f"ID: {prop[0]} | Dirección: {prop[1]} | Tipo: {prop[2]} | Precio: {prop[3]} | Estado: {prop[4]}")
                    seleccionado = prop
                    break

            if seleccionado is not None:
                return seleccionado
            else:
                print("Opción inválida. Intente nuevamente.\n")


# ---------- FUNCIONES DE MODIFICAR ----------

def modificar_inquilino(matriz):
    id_inquilino = int(input("Ingrese el ID del inquilino a modificar: "))
    for inquilino in matriz:
        if inquilino[0] == id_inquilino:
            nombre = input("Nuevo nombre: ")
            if nombre:
                inquilino[1] = nombre
            dni = input("Nuevo DNI: ")
            if dni:
                inquilino[2] = dni
            mail = input("Nuevo email: ")
            if mail:
                inquilino[3] = mail
            telefono = input("Nuevo teléfono: ")
            if telefono:
                inquilino[4] = telefono
            estado = input("Si desea dar de baja al inquilino ingrese [1] y si desea volver a activarlo [0]:")
            if estado == "1":
                estado = "Inactivo"
            elif estado == "0":
                estado = "Activo"
            else:
                print("Opción no válida. El estado no se modificará.")

            inquilino[5] = estado
            print("Inquilino modificado exitosamente.")
            return
    print("Inquilino no encontrado.")



def modificar_propiedad(matriz):
    id_propiedad = int(input("Ingrese el ID de la propiedad a modificar: "))
    for propiedad in matriz:
        if propiedad[0] == id_propiedad:
            direccion = input("Nueva dirección: ")
            if direccion:
                propiedad[1] = direccion
            tipo = input("Nuevo tipo de propiedad: ")
            if tipo:
                propiedad[2] = tipo
            precio_alquiler = input("Nuevo precio de alquiler: ")
            if precio_alquiler:
                propiedad[3] = int(precio_alquiler)
            estado = input("Si desea dar de baja la propiedad ingrese [1] y si desea volver a activarla [0]:")
            if estado == "1":
                estado = "Ocupada"
            elif estado == "0":
                estado = "Libre"
            else:
                print("Opción no válida. El estado no se modificará.")

            propiedad[4] = estado
            print("Propiedad modificada exitosamente.")
            return
    print("Propiedad no encontrada.")
