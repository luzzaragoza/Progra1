
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
        
def mostrar_matriz(encabezados, matriz):
    if matriz == []:
        print("No hay registros.\n")
        return

    for e in encabezados:
        print(e, end="\t")
    print()

    for fila in matriz:
        for elem in fila:
            print(elem, end="\t")
        print()
    print()