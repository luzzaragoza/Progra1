
def mostrar_matriz(encabezados, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for titulo in encabezados: # Imprimir encabezados
        print(titulo, end="\t")
    print()
    for fila in range(filas):
        for columna in range(columnas):
            print(matriz[fila][columna], end="\t")
        print()
