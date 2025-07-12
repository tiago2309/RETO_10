# Función que calcula la transpuesta de una matriz
def transponer_matriz(M):
    # 1) Verificamos que la matriz no esté vacía
    if len(M) == 0:
        print("Error: La matriz está vacía.")
        return []

    # 2) Verificamos que todas las filas tengan la misma cantidad de columnas
    num_columnas = len(M[0])
    for fila in M:
        if len(fila) != num_columnas:
            print("Error: La matriz no es rectangular (filas con distinta longitud).")
            return []

    # 3) Creamos la matriz transpuesta
    transpuesta = []  # Aquí guardaremos las columnas como nuevas filas
    for j in range(num_columnas):        # Recorremos columnas de la original
        nueva_fila = []
        for i in range(len(M)):          # Recorremos filas de la original
            nueva_fila.append(M[i][j])   # Intercambiamos índices: (fila, col) -> (col, fila)
        transpuesta.append(nueva_fila)   # Añadimos la nueva fila a la transpuesta

    return transpuesta


# Programa principal para probar la función
if __name__ == "__main__":
    # Matriz ejemplo (3 filas × 2 columnas)
    A = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print("Matriz original:")
    for fila in A:
        print(fila)

    print("\nMatriz transpuesta:")
    T = transponer_matriz(A)
    for fila in T:
        print(fila)
