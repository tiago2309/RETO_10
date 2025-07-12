# Función para sumar o restar dos matrices
def suma_resta_matrices(matriz1, matriz2, operacion):
    # Verificamos que las matrices tengan el mismo número de filas
    if len(matriz1) != len(matriz2):
        print("Error: Las matrices no tienen el mismo número de filas.")
        return []

    # Verificamos que todas las filas tengan el mismo número de columnas
    for i in range(len(matriz1)):
        if len(matriz1[i]) != len(matriz2[i]):
            print("Error: Las matrices no tienen el mismo número de columnas.")
            return []

    resultado = []  # Lista vacía para almacenar la matriz resultado

    # Recorremos fila por fila
    for i in range(len(matriz1)):
        fila = []  # Lista para almacenar la fila resultado
        # Recorremos elemento por elemento de la fila
        for j in range(len(matriz1[i])):
            if operacion == "suma":
                fila.append(matriz1[i][j] + matriz2[i][j])
            elif operacion == "resta":
                fila.append(matriz1[i][j] - matriz2[i][j])
            else:
                print("Operación no válida.")
                return []
        resultado.append(fila)  # Agregamos la fila a la matriz resultado

    return resultado  # Retornamos la matriz final


# Programa principal
if __name__ == "__main__":
    # Definimos las matrices que vamos a usar como ejemplo
    A = [
        [5, 3],
        [7, 0],
        [3, 8]
    ]

    B = [
        [9, 2],
        [5, 7],
        [2, 1]
    ]

    # Mostramos la suma de las matrices
    print("Suma de las matrices:")
    suma = suma_resta_matrices(A, B, "suma")
    for fila in suma:
        print(fila)

    print("\nResta de las matrices:")
    resta = suma_resta_matrices(A, B, "resta")
    for fila in resta:
        print(fila)