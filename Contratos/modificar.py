def modificar_contrato(matriz):
    id_contrato = int(input("Ingrese el ID del contrato a modificar (solo estado): "))
    for contrato in matriz:
        if contrato[0] == id_contrato:
            print("El contrato no puede modificarse, solo su estado legal.")
            estado = input("Ingrese el nuevo estado [Activo/Finalizado/Rescindido]: ").strip()
            if estado:
                contrato[6] = estado
                print("Estado del contrato actualizado.")
            else:
                print("No se ingresó ningún cambio.")
            return
    print("Contrato no encontrado.")
