        ### Strings ###
# 1
text = "Aprendiendo Python"
print(len(text))

# 2
one_str = "Hola"
two_str = "Python"
print(one_str + " " + two_str)
print(f"{one_str} {two_str}")

# 3
line_break = "Ejemplo de un\nsalto de linea"
print(line_break)

# 4
name, surname, age = "Juan David", "Angel", 32
print(f"Mi nombre es {name}, mi apellido {surname} y mi edad es {age} años.")
print("Mi nombre es {}, mi apellido {} y mi edad es {} años.".format("Juan David", "Angel", 32))

# 5
a, b, c, d, e, f = two_str
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6
word_slice = "Programación"
print(word_slice[3:7])

# 7
reversed_two_str = two_str[::-1]
print(reversed_two_str)

# 8
print(text.upper())

# 9
text_two = "Programación en Python"
print(f'Cuantas n tiene la cadena de texto "Programación en Python": {text_two.count("n")}')

# 10
three_str = "12345"
print(f'La cadena de texto "12345" es numérica: {three_str.isnumeric()}')