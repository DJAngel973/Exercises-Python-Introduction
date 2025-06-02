        ### Tuples ###
# 1
first_tuple = (10, 20, 30, 40, 50)
print(f"Creamos la primer tupla: {first_tuple}")
print(type(first_tuple))

# 2
second_tuple = (100, 200, 300, 400, 500)
print(f"Creamos una segunda  tupla: {second_tuple}")
print(f"Mostramos el segundo elemento de la segunda tupla: {second_tuple[1]}")

# 3
third_tuple = (1, 2, 3,)
print(f"Creamos una tercera tupla: {third_tuple}")
# third_tuple[0] = 10 -- TypeError: 'tuple' object does not support item assignment
print(f'Genera error al intentar modificar le primer elemento de la tercera tupla: "TypeError: (tuple) object does not support item assignment"')

# 4
quarter_tuple = (1, 2, 3, 3, 4, 5, 3)
print(f"Creamos una cuarta tupla: {quarter_tuple}")
print(f"Contamos el número 3 de la cuarta tupla, en total esta {quarter_tuple.count(3)} veces")

# 5
fifth_tuple = ("Java", "Python", "JavaScript", "Python")
print(f"Creamos una quinta tupla: {fifth_tuple}")
print(f"Encontramos el indice de la primera aparicion de Pyhon en la quinta tupla: {fifth_tuple.index('Python')}")

# 6
sixth_tuple = (1, 2, 3)
seventh_tuple = (4, 5, 6)
print(f"Creamos una sexta y septima tupla: {sixth_tuple} y {seventh_tuple}")
print(f"Concatenamos la sexta y septima tupla: {sixth_tuple + seventh_tuple}")

# 7
sub_tuple = first_tuple[2:4]
print(f"Creamos una subtupla de la primer tubla: {sub_tuple}")

# 8
eighth_tuple = ("rojo", "verde", "azul")
print(f"Creamos la octava tupla: {eighth_tuple}")
print(type(eighth_tuple))
eighth_tuple = list(eighth_tuple)
eighth_tuple[1] = "amarillo"
print(f"Convertimos la octava tupla a lista para cambiar el segundo elemento, quedando de esta forma: {eighth_tuple}, {type(eighth_tuple)}")
eighth_tuple = tuple(eighth_tuple)
print(f"Volvemos a dejar la lista en tupla: {eighth_tuple}, {type(eighth_tuple)}")

# 9
my_tuple = (1, 3, 5, 7, 9)
print(f"Tupla: {my_tuple}")
del my_tuple
# print(my_tuple) -- NameError: name 'my_tuple' is not defined.
print(f"Despues de eliminar (my_tuple) con (del), al intentar imprimirla se genera el error: NameError: name 'my_tuple' is not defined.")

# 10
nineth_tuple = (100,)
print(f"Creamos la novena tubla: {nineth_tuple}")