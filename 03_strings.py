        ### Strings ###
#1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
text_len = len(text)
print(text_len)

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
#Para poder desempaquetar los caracteres de la palabra es importante crear la misma cantidad de variable que van a tomar esa cantidad de caracteres, en este caso se necesitaron 6 variables para poder realizar el ejercicio de acuerdo al ejemplo.

#6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
first_word = "Programación"
word_slice = first_word[3:7]
print(f"Una parte de la palabra '{first_word}', posiciones 3 al 7: {word_slice}.")

#7. Invierte la cadena “Python” usando slicing y muestra el resultado.
reversed_two_str = two_str[::-1]
print(f"La palabra 'Python' invertida: {reversed_two_str}")

#8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
capital_letters = text.upper()
print(f"Convirtiendo en mayúsculas 'aprendiendo python': {capital_letters}")

#9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
text_two = "Programación en Python"
text_two_count = text_two.count("n")
print(f'Cuantas n tiene la cadena de texto "Programación en Python": {text_two_count}')

#10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
three_str = "12345"
three_str_is_number = three_str.isnumeric()
print(f'La cadena de texto "12345" es numérica: {three_str_is_number}')