        ### Hello World ###

#1. Imprime "¡Hola Mundo!", por consola.
print("Hola mundo")

#2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.
# "print()" se utiliza para mostrar en consola cualquier valor o expresión que tengamos dentro del paréntesis, con ("") o ('') indicamos que es string-str.

#3. Imprime tu nombre y edad en la misma línea utilizando la función print.
print("Soy Juan David y tengo 32 años")

#4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.
t_string = 'La ciudad es grande'
integer = 50
print(type(t_string))
print(type(integer))
print(type(4.5))
print(type(True))

#5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.
'''
type str, hace referencia a una cadena de texto.
type int, hace referencia números enteros.
type float, hace referencia números flotante o sea decimales.
con type() podemos verificar que tipo de dato es lo relacionado dentro de los paréntesis.
'''
#6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".
one_str = 'Hola'
two_str = 'Mundo.'
print(one_str, two_str)

#7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.
name = 'Pedro'
age = 30
print(f"Soy {name} y tengo {age} años")

#8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.
enter_name = input("Como te llamas?: ")
print(f"Hola {enter_name}!! gusto en saludarte.")

#9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.
#10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.
number_one = 30 # Creamos una variable del primer número para sumar.
number_two = 86 # Creamos una segunda variable del segundo número para la suma.
result = number_one + number_two # Creamos variable que guarda el resultado de la suma.
data_type_sum_numbers = type(result) # Creamos una variable donde guarda el tipo de dato del resultado.
print(f'Te enseño una pequeña suma: {number_one} + {number_two} = {result}, el tipo de dato es: "{data_type_sum_numbers}"') # Imprimimos la suma en tipo string de forma que sea entendible, concatenando todas las variables.
print("Te enseño una pequeña suma:", number_one,"+", number_two, "=", result, "el tipo de dato es:", data_type_sum_numbers) # Otra opción de concatenar, pero es menos claro.