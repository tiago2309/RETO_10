# RETO_10
Desarrollo de los ejercicios del Reto 10 (profe además me ayudaría resto media décima en el examen por eso hago los 5 ejercicios)
## 1. Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
Para este punto del Reto 11, la idea era hacer un programa que sumara o restara dos matrices, pero solo si tienen las mismas dimensiones (mismo número de filas y columnas).
Usé lo que hemos visto en clase: listas anidadas, bucles, condicionales y funciones.Primero hice una función que recibe dos matrices y una palabra clave ("suma" o "resta") y con eso arma la nueva matriz resultado. También puse validaciones para que el programa no haga nada si las dimensiones no coinciden (así no explota jaja).

```
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
```
Al final en el main puse dos matrices de ejemplo y probé tanto la suma como la resta para ver que todo funcione bien.
Todo el código está comentado para que se entienda qué hace cada parte.

```
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
```

## 2. Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
Para este punto, tocaba hacer el producto de dos matrices. Antes de arrancar, recordé (gracias al contenido que nos pasaron) que no todas las matrices se pueden multiplicar: la cantidad de columnas de la primera debe ser igual a la cantidad de filas de la segunda. Así que primero verifiqué eso.
Ya con las dimensiones bien, armé una función que multiplica "por la ley": fila por columna, sumando los productos de cada elemento que corresponde. O sea, lo clásico:
```
resultado[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][n]*B[n][j].
```

La función hace lo siguiente:
- Verifica las dimensiones.
- Recorre con tres for (uno para las filas de A, otro para las columnas de B, y otro para hacer la suma de productos).
- Retorna la matriz resultante.
Todo está bien comentado para que se entienda paso a paso.
```
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
```
Probé el código con dos matrices ejemplo (una 2×3 y una 3×2) para asegurarme de que diera bien.
Todo está hecho usando listas, for, condicionales y funciones, como lo hemos visto siempre en clase. También está todo bien comentado por si alguien quiere entender paso a paso.

```
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
```
## 3. Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.
Este punto fue tranqui (que va, me demore resto entendiendo), había que hacer la transpuesta de una matriz, que básicamente es voltear la matriz en diagonal: lo que está en filas pasa a columnas y lo que está en columnas pasa a filas. Literal cambiar los índices (i, j) por (j, i).
Para armar el código:
- Primero puse validaciones por si la matriz viene vacía o si las filas no son del mismo tamaño (uno nunca sabe, a veces se mete basura).
- Luego, recorrí las columnas de la original y fui armando las filas de la transpuesta. Con eso ya queda lista.
- La función devuelve la nueva matriz y en el main hay un ejemplo sencillo para probarla.
```
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
```
Y aquí la prueba del código:
```
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

```
## 4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.
Este punto consistía en recibir una matriz y un número de columna, y sacar la suma de los elementos de esa columna. Fácil, pero había que tener cuidado con las validaciones para que no se dañe si ponen una columna que no existe.

Para resolverlo:
- Revisé que la matriz no estuviera vacía y que el índice de columna fuera válido.
- Después, recorrí la matriz fila por fila y sumé el valor que estaba en esa columna.
- Está hecho con funciones, bien claro y comentado como pidió el profe. Probé con una matriz de ejemplo y todo fluyó.
```
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
```
Prueba del código:
```
# Ejemplo de uso:
matriz_ejemplo = [
    [2, 4, 6],
    [1, 3, 5],
    [0, 7, 8]
]

columna_a_sumar = 1
resultado = sumar_columna(matriz_ejemplo, columna_a_sumar)
print(f"La suma de la columna {columna_a_sumar} es: {resultado}")

```
## 5.Desarrollar un programa que sume los elementos de una fila dada de una matriz.

(llegamos al último punto por fiiin jaja) 
Este es parecido al anterior, pero ahora la suma es por fila. Recibimos una matriz y el número de la fila, y devolvemos la suma de todos los elementos que hay en esa fila.

La lógica fue:
- Primero validar que la matriz no esté vacía y que el número de fila sea válido.
- Luego usamos sum() sobre esa fila específica para que sea más limpio y corto el código.

```
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
```
Probamos el código:
```
# Ejemplo de uso:
matriz_ejemplo = [
    [2, 4, 6],
    [1, 3, 5],
    [0, 7, 8]
]

fila_a_sumar = 2
resultado = sumar_fila(matriz_ejemplo, fila_a_sumar)
print(f"La suma de la fila {fila_a_sumar} es: {resultado}")

```
 y yap, eso sería todo, profeee deme esos puntos extra porfa jajaja
