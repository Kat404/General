
# ! TUTORIAL DE PYTHON
# ? ---> VARIABLES <---
nombre = 'Jose Luis'
edad = 19
altura = 1.70
es_estudiante = True
# * 'nombre', 'edad', 'altura' y 'es_estudiante' son los nombres de nuestras variables.

# * Dichas variables almacenan datos diferentes:

# * 'nombre' almacena una cadena de caracteres (str). Ejemplos de cadenas son: 'Jose Luis', 'Hola', 'Python'.
# * 'edad' almacena un número entero (int). Ejemplos de enteros son: 19, 20, -10.
# * 'altura' almacena un número decimal (float). Ejemplos de decimales son: 1.70, 3.14, -0.5.
# * 'es_estudiante' almacena un valor booleano (bool). Ejemplos de booleanos son: True, False.
# * 'True' significa verdadero y 'False' significa falso.

# ? ---> PRINT <---
print('Hola, soy ', nombre,'tengo', edad, 'años y mido', altura, 'metros.')
print('¿Soy estudiante?', es_estudiante)

# * Con 'print' mostramos en pantalla el contenido de nuestras variables.
# * La función 'print' nos permite mostrar en pantalla cualquier tipo de dato.
# * En este caso, mostramos una cadena de caracteres y el contenido de nuestras variables.
# * La función 'print' puede recibir varios argumentos separados por comas.

# ? ---> F-STRINGS <---
mensaje = f"Hola, soy {nombre}, tengo {edad} y mido {altura} metros."
print(mensaje)
# ó
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura} metros.")

# * Los f-strings son cadenas de texto que empiezan con una 'f' antes de las comillas y te permiten
# * insertar variables directamente dentros de ellas usando llaves "{}".
# ? Útil en texto largos o repetitivos.

# ? ---> TYPE <---
x = 10
print(type(x)) # <class 'int'>

y = 3.1416
print(type(y)) # <class 'float'>

z = 'Hola'
print(type(z)) # <class 'str'>

w = True
print(type(w)) # <class 'bool'>

# * La función 'type' nos permite conocer el tipo de dato de una variable.
# * En este caso, mostramos el tipo de dato de las variables 'x', 'y', 'z' y 'w'.


# ? ---> OPERADORES <---
# * Operadores Aritméticos/Matemáticos
a = 5
b = 2
print(a + b) # Suma: 7
print(a - b) # Resta: 3
print(a * b) # Multiplicación: 10
print(a / b) # División: 2.5
print(a // b) # División entera: 2
print(a % b) # Módulo: 1
print(a ** b) # Potencia: 25

# * Los operadores son símbolos que realizas operaciones en valores y variables.
# * Los operadores aritméticos son: 
# * + (suma),
# * - (resta),
# * * (multiplicación),
# * / (división). 
# * // (división entera: solo devuelve la parte entera),
# * % (módulo, devuelve el resto de la divisón), 
# * ** (exponenciación).

# * Operadores de Comparación
x = 10
y = 5
print(x == y) # Salida: False
print(x != y) # Salida: True
print(x > y) # Salida: True
print(x < y) # Salida: False
print(x >= y) # Salida: True
print(x <= y) # Salida: False

# * Los operadores de comparación devuelven un valor booleano (True o False).
# * Estos sirven para comparar los valores de nuestras variables.

# * Operadores Lógicos
p = True
q = False
print(p and q) # Salida: False
print(p or q) # Salida: True
print(not p) # Salida: False

# * -> and ('y' lógico): Devuelve True si ambas condiciones son verdaderas.
# * -> or ('o' lógico): Devuelve True si al menos una de las condiciones es verdadera.
# * -> not ('no' lógico): Invierte el valor de una condición (si es True devuelve False, y viceversa).

# ! -----------------------------------------------------------------------------------------------------

# ? ---> CONTROL DE FLUJO <---
edad1 = 17
if edad1 >= 18:
    print("Eres mayor de edad.")
elif edad1 == 17:
    print("Te falta poco para ser mayor de edad.")
else:
    print("Eres menor de edad.")

# * El control de flujo te permite decidir qué partes de tu código se ejecutan y en qué orden.
# * Sentencias 'if', 'elif', 'else' (condicionales): Permite ejecutar diferentes bloques de código
# * según si una condición es verdadera o falsa.

# * 'if' evalúa una condición. Si es verdadera, se ejecuta el bloque de código indentado debajo.
# * 'elif' (abreviatura del "else if") se evalúa si la condición anterior del if fue falsa. Puedes tener múltiples 'elif'.
# * 'else' se ejecuta si ninguna de las condiciones anteriores ('if' o 'elif') fue verdadera.


# ? ---> BUCLES FOR <---
# * Ejemplo con un rango de números:
for i in range(5): # range(5) genera una secuencia de 0 a 4
    print(i) # Salida: 0, 1, 2, 3, 4

# * Ejemplo con una lista:
frutas = ["manzana", "banana", "pera"]
for fruta in frutas:
    print(f"Me gusta la {fruta}") # Salida: Me gusta la manzana, Me gusta la banana, Me gusta la pera.

# * Permiten repetir un bloque de código un cierto número de veces o para cada elemento de una secuencia (como una lista o una cadena).

# ? ---> BUCLES WHILE <---
contador = 0
while contador < 5:
    print(contador) # Salida: 0, 1, 2, 3, 4
    contador = contador + 1 # Incrementa el contador en 1 en cada iteración.

# * Repite un bloque de código mientras una condición sea verdadera.

# ! ------------------------------------------------------------------------------------------------------------------

# ? ---> ESTRUCTURAS DE DATOS <---
# * Las estructuras de datos permiten organizar y almacenar colecciones de datos.

# ? ---> LISTAS <---
mi_lista = [1, 2, "tres", True, 3.14]
print(mi_lista[0]) # Salida: 1 (los índices empiezan en 0)
print(mi_lista[2]) # Salida: "tres"
mi_lista.append("Nuevo elemento") # Añade un elemento al final
print(mi_lista) # Salida: [1, 2, 'tres', True, 3.14, 'Nuevo elemento']
mi_lista[1] = "dos" # Modifica el elemento en el índice 1
print(mi_lista) # Salida: [1, 'dos', 'tres', True, 3.14, 'Nuevo elemento']
# * Listas: Son colecciones ordenadas de elementos. Pueden contener elementos de diferentes tipos. Son mutables, lo que significa
# * que puedes cambiar sus elementos después de crearlas. Se definen con corchetes [].

# ? ---> TUPLAS <---
mi_tupla = (1, 2, "tres")
print(mi_tupla[0]) # Salida: 1
# ! mi_tupla[0] = 10 # Esto generaría un error porque las tuplas son inmutables.
# * Tuplas: Son similares a las listas, pero son inmutables, lo que significa que no puedes modificar sus elementos después de crearlas. Se definen con paréntesis ().

# ? ---> DICCIONARIOS <---
mi_diccionario = {
    "nombre": "Jose Luis",
    "edad": 19,
    "ciudad": "Morelia"
}
print(mi_diccionario["nombre"]) # Salida: "Jose Luis"
print(mi_diccionario.get("edad")) # Salida: 19
mi_diccionario["profesion"] = "Estudiante" # Añade un nuevo par clave-valor
print(mi_diccionario) # Salida: {'nombre': 'Jose Luis', 'edad': 19, 'ciudad': 'Morelia', 'profesion': 'Estudiante'}
# * Son colecciones de pares clave-valor. Cada elemento tiene una clave única y un valor asociado. Se definen con llaves {}.

# ? ---> FUNCIONES <---
def saludar(nombre):
    """! Esta función saluda a la persona con el nombre proporcionado."""
    print(f"Hola, {nombre}!")
# Llamar a la función
saludar("Jose Luis") # Salida: Hola, Jose Luis!
saludar("Martha") # Salida: Hola, Martha!
# * Una función es un bloque de código reutilizable que realiza una tarea específica.
# * Las funciones te ayudan a organizar tu código y hacerlo más fácil de leer y mantener.
# * Se definen con la palabra clave 'def' seguida del nombre de la función y paréntesis (). Pueden contener parámetros (entradas de la función), y dos puntos :.
# * El bloque de código de la función debe estar indentado.
# ? La línea dentro de las triples comillas es un comentario que describe lo que hace la función. Es opcional, pero es una buena práctica incluirlo para documentar tu código.
# * Puedes 'llamar' a la función con diferentes argumentos (valores de entrada) para obtener diferentes resultados.

# * Las funciones también pueden devolver valores usando la palabra clave 'return'.
def sumar(a, b):
    """* Esta función devuelve la suma de dos números."""
    suma = a + b
    return suma

resultado = sumar(5, 3) # Llamar a la función y almacenar el resultado en una variable
print(resultado) # Salida: 8

# ! ------------------------------------------------------------------------------------------------------------------

# ? ---> MÓDULOS Y BIBLIOTECAS <---
import math # Importa el módulo 'math' que contiene funciones matemáticas.
print(math.sqrt(16)) # Salida: 4.0 (raíz cuadrada de 16)
print(math.pi) # Salida: 3.141592653589793 (valor de pi)

import random # Importa el módulo 'random' que contiene funciones para generar números aleatorios.
print(random.randint(1, 10)) # Salida: Un número aleatorio entre 1 y 10.
# * Un módulo es un archivo que contiene código Python (funciones, clases, variables, etc.) que puedes usar en tus propios programas.
# * Una biblioteca es una colección de módulos relacionados que proporcionan funcionalidades específicas.
# * Python tiene una gran cantidad de módulos y bibliotecas incorparadas y de terceros que te permiten hacer muchas cosas sin tener que escribir todo el código desde cero.
# ? Para usar un módulo, debes importarlo usando la palabra clave 'import' seguida del nombre del módulo.

from datetime import date # Importa la clase 'date' del módulo 'datetime'.
hoy = date.today() # Obtiene la fecha actual.
print(hoy) # Salida: 2023-10-05 (o la fecha actual en formato YYYY-MM-DD)
# * Puedes importar solo partes específicas de un módulo usando 'from ... import ...'.

# ! ------------------------------------------------------------------------------------------------------------------

# ? ---> ENTRADA Y SALIDA (INPUT/OUTPUT) <---
nombre = input("Por favor, introduce tu nombre: ") # Solicita al usuario que introduzca su nombre.
print(f"Hola, {nombre}!") # Salida: Hola, [nombre del usuario]!
# * La función 'input' permite recibir datos del usuario a través de la consola. El texto dentro de los paréntesis es el mensaje que se muestra al usuario.

edad_str = input("Por favor, introduce tu edad: ") # Solicita al usuario que introduzca su edad.
edad = int(edad_str) # Convierte la cadena de texto a un número entero.
print(f"Tienes {edad} años.") # Salida: Tienes [edad del usuario] años.

# * La función 'input' siempre devuelve una cadena de texto, por lo que si necesitas un número, debes convertirlo usando 'int()' o 'float()' según el tipo de dato que necesites.
# * En este caso, convertimos la cadena de texto a un número entero usando 'int()'.
# * print(): Ya hemos usando 'print()' para mostrar mensajes en la consola.
# * input(): La funcioón 'input()' te permite pedir información al usuario. El programa se detendrá y esperará
# * a que el usuario introduzca un valor y presione 'Enter'.
# ! La función 'input()' siempre devuelve un valor de tipo cadena (str), por lo que si necesitas un número, debes convertirlo a int o float.

# ! ------------------------------------------------------------------------------------------------------------------

# ? ---> MANEJO BÁSICO DE ERRORES (TRY-EXCEPT) <---
try:
    numero_str = input("Introduce un número: ") # Solicita al usuario que introduzca un número.
    numero = int(numero_str) # Intenta convertir la cadena a un número entero.
    resultado = 10 / numero # Intenta dividir 10 entre el número introducido.
    print(f"El resultado es: {resultado}") # Muestra el resultado.
except ValueError:
    print("Error: Debes introducir un número válido.") # Maneja el error si la conversión falla.
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.") # Maneja el error si el número es cero.
except Exception as e:
    print(f"Error inesperado: {e}") # Maneja cualquier otro error inesperado.
# * El bloque 'try' contiene el código que puede generar un error. Si ocurre un error, el flujo del programa se detiene y se pasa al bloque 'except' correspondiente.
# * Puedes tener múltiples bloques 'except' para manejar diferentes tipos de errores.
# * 'Exception' es un tipo de error general que captura cualquier error no manejado por los bloques 'except' anteriores.
# * El 'as e' te permite capturar el error y usarlo dentro del bloque 'except' para mostrar un mensaje más específico.

# ! Fin del tutorial básico de Python.
# * Este tutorial cubre los conceptos básicos de Python, incluyendo variables, tipos de datos, operadores, control de flujo,
# * estructuras de datos, funciones, módulos y manejo de errores.
# * Con estos conceptos, deberías tener una buena base para comenzar a programar en Python.
# ? Recuerda que la práctica es clave para mejorar tus habilidades de programación. ¡Diviértete programando!