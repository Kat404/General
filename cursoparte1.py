# ---> CURSO PARTE 1 UDEMY <---
print("Hola Mundo") # Para imprimir podemos usar comillas dobles o simples ("") o (''), dependerá del gusto del usuario usar uno u otro.


# Validación del nombre (no debe contener números)
while True:
    nombre = input('Bienvenido, ¿cuál es tu nombre?: \n> ') #El 'input' pregunta al usuario un valor, en este caso su nombre.
    # Verificamos que el nombre solo contenga letras y espacios
    if all(c.isalpha() or c.isspace() for c in nombre) and nombre.strip() != "":
        print(f'Hola {nombre}!') # Se imprime el nombre que el usuario proporciona.
        break
    else:
        print("Error: El nombre debe contener solo letras y espacios. Inténtalo de nuevo.")

# Validación de la edad (debe ser un número entero)
while True:
    try:
        edad = int(input('¿Cuál es tu edad?: \n>  ')) # Se convierte la edad a un número entero porque el input devuelve un string
        print(f'Tienes {edad} años de edad, ¡genial!') # Se imprime la edad del usuario ya convertido de 'str' --> 'int'.
        break
    except ValueError:
        print("Error: Debes introducir un número entero para la edad. Inténtalo de nuevo.")

# Validación de la altura (debe ser un número, puede ser decimal)
while True:
    altura = input('¿Y cuánto mides? (metros):  \n> ') # Se le pregunta al usuario su altura
    try:
        # Intentamos convertir a float para verificar que sea un número
        float(altura.replace(',', '.'))  # Reemplazamos comas por puntos para aceptar ambos formatos
        print(f'Así que mides {altura} metros, muy bien!') # Se imprime la altura del usuario.
        break
    except ValueError:
        print("Error: Debes introducir un número válido para la altura. Inténtalo de nuevo.")

print(type(nombre)) # Se imprime el tipo de dato de la variable 'nombre' que es 'str'.
print(type(edad)) # Se imprime el tipo de dato de la variable 'edad' que es 'int' porque se convirtió a 'int' en la línea 9.
print(type(altura)) # Se imprime el tipo de dato de la variable 'altura' que es 'str'.


# Nota: Para comentar muchas líneas de código utilizamos triples comillas dobles ("""")
# Ejemplo de comentario en bloque
""" Hola
    soy un comentario
    en bloque
"""

variable1 = 15 # Esta variable puede tener todo tipo de dato sin necesidad de especificarlo, a diferencia de otros lenguajes.
print(variable1) # Se imprime el valor de la variable1.

import constantes # Se importa el módulo 'constantes' que contiene las constantes definidas en el archivo 'constantes.py'.
# Se pueden importar módulos de Python o crear los propios.
print(constantes.PI) # Se imprime el valor de la constante PI definida en el módulo 'constantes'.

variable2 = variable3 = variable4 = "Python es chido." # Se pueden asignar el mismo valor a varias variables al mismo tiempo.
print(variable2) # Se imprime el valor de la variable2.
print(variable3) # Se imprime el valor de la variable3.
print(variable4) # Se imprime el valor de la variable4.

name1, name2, name3 = "Jose", "Pardo", "Daniel" # Se pueden definir varias variables en la misma línea de código con valores diferentes.
# Se usan más comúnmente lista y/o diccionarios para almacenar muchos datos en diferentes variables.
print(name1)
print(name2)
print(name3)

# Ejemplo de lista
lista = ["manzana", "naranja", "banana"]
print(lista)  # Salida: ['manzana', 'naranja', 'banana']
"""
Las listas son colecciones ordenadas y modificables que permiten elementos duplicados.
Se definen con corchetes [] y sus elementos se separan por comas.
"""

# Ejemplo de diccionario
diccionario = {"nombre": "Jose", "edad": 19, "altura": 1.71}
print(diccionario)  # Salida: {'nombre': 'Jose', 'edad': 19, 'altura': 1.71}
"""
Los diccionarios son colecciones desordenadas, modificables e indexadas por claves.
Se definen con llaves {} y contienen pares clave-valor separados por comas.
"""

# Ejemplo de tupla
tupla = ("manzana", "naranja", "banana")
print(tupla)  # Salida: ('manzana', 'naranja', 'banana')
"""
Las tuplas son colecciones ordenadas e inmutables que permiten elementos duplicados.
Se definen con paréntesis () y sus elementos se separan por comas.
"""

# Ejemplo de set
conjunto = {"manzana", "naranja", "banana"}
print(conjunto)  # Salida: {'naranja', 'manzana', 'banana'} (el orden puede variar)
"""
Los sets son colecciones desordenadas y no indexadas que no permiten elementos duplicados.
Se definen con llaves {} y sus elementos se separan por comas.
"""

# Ejemplo de rango
rango = range(10)
print(rango)  # Salida: range(0, 10)
"""
Range genera una secuencia inmutable de números, comúnmente utilizada en bucles for.
En este caso, genera números del 0 al 9 (10 números en total).
"""

# Ejemplo de booleano
booleano = True
print(booleano)  # Salida: True
"""
Los booleanos representan uno de dos valores: True o False.
Se utilizan en expresiones condicionales y operaciones lógicas.
"""

# Ejemplo de None
none = None
print(none)  # Salida: None
"""
None representa la ausencia de valor o un valor nulo en Python.
Se utiliza comúnmente para inicializar variables que aún no tienen un valor específico.
"""

# Ejemplo de bytes
bytes = b"Hola"
print(bytes)  # Salida: b'Hola'
"""
Los bytes son secuencias inmutables de bytes individuales.
Se utilizan para representar datos binarios o texto codificado.
"""

# Ejemplo de complex
complex = 1j
print(complex)  # Salida: 1j
"""
Los números complejos tienen una parte real y una parte imaginaria.
Se representan con la letra 'j' o 'J' para indicar la parte imaginaria.
"""

# Ejemplo de float
float = 1.5
print(float)  # Salida: 1.5
"""
Los números de punto flotante representan números decimales.
Pueden representar números muy grandes o muy pequeños con notación científica.
"""

# Ejemplo de int
int = 1
print(int)  # Salida: 1
"""
Los enteros son números sin parte decimal.
En Python 3, los enteros pueden ser de tamaño ilimitado.
"""

# Ejemplo de str
str = "Hola"
print(str)  # Salida: Hola
"""
Las cadenas son secuencias inmutables de caracteres.
Se pueden definir con comillas simples o dobles.
"""