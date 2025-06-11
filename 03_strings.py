        ### Strings ###
#1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

#2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
one_str = "Hola"
two_str = "Python"
print(one_str + " " + two_str)
print(f"{one_str} {two_str}")

#3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
line_break = "Ejemplo de un\nsalto de linea"
print(line_break)

#4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
name, surname, age = "Juan David", "Angel", 32
print(f"Mi nombre es {name}, mi apellido {surname} y mi edad es {age} años.")
print("Mi nombre es {}, mi apellido {} y mi edad es {} años.".format("Juan David", "Angel", 32))

#5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
a, b, c, d, e, f = two_str
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
word_slice = "Programación"
print(word_slice[3:7])

#7. Invierte la cadena “Python” usando slicing y muestra el resultado.
reversed_two_str = two_str[::-1]
print(reversed_two_str)

#8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
print(text.upper())

#9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
text_two = "Programación en Python"
print(f'Cuantas n tiene la cadena de texto "Programación en Python": {text_two.count("n")}')

#10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
three_str = "12345"
print(f'La cadena de texto "12345" es numérica: {three_str.isnumeric()}')