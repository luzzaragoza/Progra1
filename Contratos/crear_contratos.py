from Contratos.validaciones_contratos import validar_id, validar_fecha, validar_monto_mensual

def _pedir(mensaje, validador, convertir=int):
    """
    Muestra un mensaje, pide un dato por teclado y valida la entrada.
    Repite hasta que el valor cumpla la validación y luego lo devuelve convertido.
    """
    while True:
        s = input(mensaje).strip()
        if validador(s):
            return convertir(s)
        print("Valor inválido, probá de nuevo.")

def crear_matriz_contrato(cant_contratos):
    """
    Crea una lista de contratos a partir de los datos ingresados por el usuario.

    Cada contrato se guarda como una lista con el siguiente formato:
    [ID Contrato, ID Propiedad, ID Inquilino, Fecha Inicio, Fecha Fin, Monto mensual, Estado]

    Funcionamiento:
    - Pide la cantidad de contratos a crear (parámetro cant_contratos).
    - Genera un ID de contrato automático para cada nuevo contrato,
      arrancando en 1 y sumando de a uno por cada fila creada.
    - Solicita al usuario el ID de la propiedad, el ID del inquilino,
      la fecha de inicio, la fecha de fin, el monto mensual y el estado de actividad.
    - Valida cada dato usando funciones del módulo validaciones_contratos:
        * validar_id → asegura que IDs sean enteros positivos.
        * validar_fecha → asegura que las fechas tengan formato YYYY-MM-DD.
        * validar_monto_mensual → asegura que el monto sea un entero positivo.
    - Si el dato no es válido, vuelve a pedirlo hasta que lo sea.
    - Devuelve una lista (matriz) con todos los contratos creados.

    Parámetros:
        cant_contratos (int): cantidad de contratos a crear.

    Retorna:
        lista: matriz con los contratos creados y validados.
    """
    contratos = []
    for i in range(cant_contratos):
        ID_contrato  = len(contratos) + 1
        id_propiedad = _pedir("ID de la propiedad: ", validar_id, int)
        id_inquilino = _pedir("ID del inquilino: ", validar_id, int)
        fecha_inicio = _pedir("Fecha de inicio (YYYY-MM-DD): ", validar_fecha, str)
        fecha_fin    = _pedir("Fecha de fin (YYYY-MM-DD): ", validar_fecha, str)
        monto_mensual= _pedir("Monto mensual (entero): ", validar_monto_mensual, int)

        contratos.append([ID_contrato, id_propiedad, id_inquilino, fecha_inicio, fecha_fin, monto_mensual, True])
    return contratos


'''def crear_matriz_contrato(cant_contratos):
    """
    Crea una matriz con contratos según la cantidad pedida.

    Formato de cada contrato:
    [ID Contrato, ID Propiedad, ID Inquilino, Fecha Inicio, Fecha Fin, Monto mensual, Estado]
    """
    contratos = []

    for i in range(cant_contratos):
        # ID automático con lambda
        generar_id = lambda: len(contratos) + 1  
        ID_contrato = generar_id()

        id_propiedad = input("ID de la propiedad: ").strip()
        id_inquilino = input("ID del inquilino: ").strip()
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ").strip()
        fecha_fin    = input("Fecha de fin (YYYY-MM-DD): ").strip()
        monto_mensual= input("Monto mensual: ").strip()

        # Creamos el contrato como lista
        contrato = [ID_contrato, id_propiedad, id_inquilino, fecha_inicio, fecha_fin, monto_mensual, True]

        # Lo agregamos a la matriz
        contratos.append(contrato)

    return contratos
'''