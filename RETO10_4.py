def sumar_columna(matriz, col):
    """
    Función que suma todos los elementos de una columna específica.
    :param matriz: lista de listas (matriz)
    :param col: índice de la columna a sumar (entero)
    :return: suma de los elementos de esa columna
    """
    # Validación: asegurarse de que la matriz no esté vacía
    if len(matriz) == 0:
        return "La matriz está vacía."

    # Validación: verificar que la columna existe en todas las filas
    for fila in matriz:
        if col >= len(fila) or col < 0:
            return "Columna fuera del rango."

    # Acumular la suma de los elementos en la columna dada
    suma = 0
    for fila in matriz:
        suma += fila[col]

    return suma

# Ejemplo de uso:
matriz_ejemplo = [
    [2, 4, 6],
    [1, 3, 5],
    [0, 7, 8]
]

columna_a_sumar = 1
resultado = sumar_columna(matriz_ejemplo, columna_a_sumar)
print(f"La suma de la columna {columna_a_sumar} es: {resultado}")
