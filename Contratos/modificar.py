def modificar_contrato(matriz):
    id_contrato = int(input("Ingrese el ID del contrato a gestionar: "))
    for contrato in matriz:
        if contrato[0] == id_contrato:
            print("\nAcciones disponibles:")
            print("1 - Finalizar contrato")
            print("2 - Rescindir contrato")
            print("3 - Renovar contrato")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                contrato[6] = "Finalizado"
                print("Contrato finalizado correctamente.")
            
            elif opcion == "2":
                contrato[6] = "Rescindido"
                print("✅ Contrato rescindido correctamente.")
            
            elif opcion == "3":
                # marcar el contrato viejo como finalizado
                contrato[6] = "Finalizado"
                
                fecha_inicio = input("Nueva fecha de inicio (YYYY-MM-DD): ").strip()
                fecha_fin    = input("Nueva fecha de fin (YYYY-MM-DD): ").strip()
                monto        = input("Nuevo monto mensual: ").strip()

                if fecha_inicio and fecha_fin and monto:
                    nuevo_id = len(matriz) + 1
                    nuevo_contrato = [
                        nuevo_id,
                        contrato[1],   # misma propiedad
                        contrato[2],   # mismo inquilino
                        fecha_inicio,
                        fecha_fin,
                        int(monto),
                        "Activo"
                    ]
                    matriz.append(nuevo_contrato)
                    print("Contrato renovado correctamente (nuevo ID generado).")
                else:
                    print("Faltan datos, no se generó renovación.")
            
            else:
                print("Opción inválida.")
            return
    
    print("Contrato no encontrado.")
