# Función para multiplicar dos matrices
def producto_matrices(A, B):
    # Para multiplicar A (m × n) por B (n × p) se necesita que
    # el número de columnas de A sea igual al número de filas de B
    if len(A[0]) != len(B):
        print("Error: No se puede multiplicar. "
              "Las columnas de A deben ser igual a las filas de B.")
        return []

    resultado = []  # Aquí guardamos la matriz resultante (m × p)

    # Recorremos cada fila de A
    for i in range(len(A)):
        fila_resultado = []  # Fila que iremos construyendo

        # Recorremos cada columna de B
        for j in range(len(B[0])):
            # Calculamos la entrada (i, j) haciendo la suma de productos
            suma_productos = 0
            for k in range(len(B)):          # k recorre la columna de A y la fila de B
                suma_productos += A[i][k] * B[k][j]
            fila_resultado.append(suma_productos)

        resultado.append(fila_resultado)  # Añadimos la fila completa

    return resultado


# Programa principal para probar la función
if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]  # A es 2 × 3

    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]  # B es 3 × 2

    print("Producto A × B:")
    C = producto_matrices(A, B)
    for fila in C:
        print(fila)
