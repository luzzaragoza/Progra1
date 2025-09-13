
def convertir_a_texto(valor):      
    """
    Convierte valores a string. 
    Si es un número entero, lo devuelve con separador de miles (250000 -> 250.000)
    En caso contrario, devuelve el texto tal cual.
    """
    entrada=str(valor)
    if entrada.isdigit():    #solo números enteros positivos
        return f"{int(entrada):,}".replace(",",".")
    return entrada

def estado_a_texto(b):
    """
    Convierte un valor booleano en una representación textual del estado.
    Parámetros:
        b (boolean): valor booleano que indica el estado lógico.
                  True  -> el registro está activo
                  False -> el registro está inactivo

    Retorna:
        string: "Activo" si b es True, "Inactivo" si b es False.
    """
    return "Activo" if b else "Inactivo"

def linea_tabla(anchos, sep_izq="+", sep_med="+", sep_der="+", relleno="-"):
    """
    Genera una línea separadora de la tabla según los anchos de columna.
    """
    return sep_izq + sep_med.join(relleno * (ancho + 2) for ancho in anchos) + sep_der

def mostrar_matriz(encabezados, matriz, pos_mil=None):
    """
    Muestra una matriz como tabla con bordes, encabezados y columnas alineadas.
    Texto alineado a la izquierda.
    Números alineados a la derecha.
    Si la matriz está vacía, muestra "No hay registros".
    pos_mil: conjunto de posiciones (índices de columna) donde aplicar separador de miles.   
    """

    if not matriz:
        print("No hay registros. \n")
        return
    if pos_mil is None:
        pos_mil=set()
    
    num_cols= len(encabezados)
    filas=[fila[:num_cols]+[""] * max(0, num_cols - len(fila)) for fila in matriz]

    #Calcular anchos por columna (incluyendo los encabezados)

    anchos=[]

    for c in range(num_cols):     #c de columna en numeros de columnas
        ancho_col = len(str(encabezados[c]))
        for fila in filas:
            valor = fila[c]
            if valor is True or valor is False:           # <-- convierte booleans
                valor = estado_a_texto(valor)
            ancho_col = max(ancho_col, len(convertir_a_texto(valor)))
        anchos.append(ancho_col)   

    #Encabezado 
    print(linea_tabla(anchos))
    encabezado_formt= "| " + " | ".join(str(encabezados[i]).ljust(anchos[i]) for i in range (num_cols))+ " |"
    print(encabezado_formt)
    print(linea_tabla(anchos, "+", "+", "+", "="))
    
    #Filas
    for fila in filas:
        celdas=[]
        for j in range(num_cols):
            valor = fila[j]
            if valor is True or valor is False:                    # <-- convierte booleans
                valor = estado_a_texto(valor)
            crudo = str(valor)
            es_num = crudo.isdigit()                   #Se decide como se alinea según el valor original
            if j in pos_mil and es_num:
                texto = convertir_a_texto(crudo)
            else:
                texto = crudo
            celdas.append(texto.rjust(anchos[j]) if es_num else texto.ljust(anchos[j]))
        print("| " + " | ".join(celdas) + " |")

    print(linea_tabla(anchos))
    print()

    
        

