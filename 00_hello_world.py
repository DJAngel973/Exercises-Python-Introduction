        ### Hello World ###

# 1 y 2
print("Hola mundo")
# "print()" se utiliza para mostrar en consola cualquier valor o expresion que tengamos dentro del parentesis, con ("") o ('') indicamos que es string-str.

# 3
print("Soy Juan David y tengo 32 años")

# 4
t_string = 'La ciudad es grande'
integer = 50
print(type(t_string))
print(type(integer))
print(type(4.5))
print(type(True))

# 5
'''
type str, hace referencia a una cadena de texto.
type int, hace referencia numeros enteros.
type float, hace referencia numeros flotante osea decimales.
con type() podemos verificar que tipo de dato es lo relacionado dentro de los parentesis.
'''
# 6
one_str = 'Hola'
two_str = 'Mundo.'
print(one_str, two_str)

# 7
name = 'Pedro'
age = 30
print(f"Soy {name} y tengo {age} años")

# 8
enter_name = input("Como te llamas?: ")
print(f"Hola {enter_name}!! gusto en saludarte.")

# 9 y 10
number_one = 30 # Creamos una variable del primer numero para sumar.
number_two = 86 # Creamos una segunda variable del segundo numero para la suma.
result = number_one + number_two # Creamos variable que guarda el resultado de la suma.
data_type_sum_numbers = type(result) # Creamos una variable donde guarda el tipo de dato del resultado.
print(f'Te enseño una pequeña suma: {number_one} + {number_two} = {result}, el tipo de dato es: "{data_type_sum_numbers}"') # Imprimimos la suma en tipo string de forma que sea entendible, concatenando todas las variables.
print("Te enseño una pequeña suma:", number_one,"+", number_two, "=", result, "el tipo de dato es:", data_type_sum_numbers) # Otra opcion de cocatenar, pero es menos claro.