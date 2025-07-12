def sumar_fila(matriz, fila):
    """
    Función que suma todos los elementos de una fila específica.
    :param matriz: lista de listas (matriz)
    :param fila: índice de la fila a sumar (entero)
    :return: suma de los elementos de esa fila
    """
    # Validación: asegurar que la matriz no esté vacía
    if len(matriz) == 0:
        return "La matriz está vacía."

    # Validación: verificar que la fila esté dentro del rango válido
    if fila < 0 or fila >= len(matriz):
        return "Fila fuera del rango."

    # Sumar todos los elementos de la fila indicada
    suma = sum(matriz[fila])
    return suma

# Ejemplo de uso:
matriz_ejemplo = [
    [2, 4, 6],
    [1, 3, 5],
    [0, 7, 8]
]

fila_a_sumar = 2
resultado = sumar_fila(matriz_ejemplo, fila_a_sumar)
print(f"La suma de la fila {fila_a_sumar} es: {resultado}")
