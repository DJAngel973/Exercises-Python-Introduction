        ### Tuples ###
#1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.-Create a tuple with the values (10, 20, 30, 40, 50) and print it.
first_tuple = (10, 20, 30, 40, 50)
print(f"Creamos la primer tupla: {first_tuple}")
print(type(first_tuple))

#2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.-Access the second element of the tuple (100, 200, 300, 400, 500) and show it.
second_tuple = (100, 200, 300, 400, 500)
print(f"Creamos una segunda  tupla: {second_tuple}")
print(f"Mostramos el segundo elemento de la segunda tupla: {second_tuple[1]}")

#3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.-Try to modify the first element of the tuple (1, 2, 3) to 10 and observe the result.
third_tuple = (1, 2, 3,)
print(f"Creamos una tercera tupla: {third_tuple}")
# third_tuple[0] = 10 -- TypeError: 'tuple' object does not support item assignment
print(f'Genera error al intentar modificar le primer elemento de la tercera tupla: "TypeError: (tuple) object does not support item assignment"')

#4. Cuenta cuantas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).-Count how many times the number 3 appears in the tuple (1, 2, 3, 3, 4, 5, 3).
quarter_tuple = (1, 2, 3, 3, 4, 5, 3)
print(f"Creamos una cuarta tupla: {quarter_tuple}")
print(f"Contamos el número 3 de la cuarta tupla, en total esta {quarter_tuple.count(3)} veces")

#5. Encuentra el índice de la primera aparición de la cadena 'Python' en la tupla ("Java", "JavaScript", "Python").
# Find the index of the first appearance of the 'Python' chain in the tuple ("Java", "JavaScript", "Python").
fifth_tuple = ("Java", "Python", "JavaScript", "Python")
print(f"Creamos una quinta tupla: {fifth_tuple}")
print(f"Encontramos el indice de la primera aparicion de Pyhon en la quinta tupla: {fifth_tuple.index('Python')}")

#6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
# Concatenate two tuples: (1, 2, 3) and (4, 5, 6) and print the resulting tuple.
sixth_tuple = (1, 2, 3)
seventh_tuple = (4, 5, 6)
print(f"Creamos una sexta y septima tupla: {sixth_tuple} y {seventh_tuple}")
print(f"Concatenamos la sexta y septima tupla: {sixth_tuple + seventh_tuple}")

#7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
# Create a subtuple with the elements from position 2 to 4 (not including the 4) of the tuple (10, 20, 30, 40, 50).
sub_tuple = first_tuple[2:4]
print(f"Creamos una subtupla de la primer tubla: {sub_tuple}")

#8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
# Turn the tuple ("red", "green", "blue") into a list, change the second element to "yellow" and turn it again into a tuple. Print the resulting tuple.
eighth_tuple = ("rojo", "verde", "azul")
print(f"Creamos la octava tupla: {eighth_tuple}")
print(type(eighth_tuple))
eighth_tuple = list(eighth_tuple)
eighth_tuple[1] = "amarillo"
print(f"Convertimos la octava tupla a lista para cambiar el segundo elemento, quedando de esta forma: {eighth_tuple}, {type(eighth_tuple)}")
eighth_tuple = tuple(eighth_tuple)
print(f"Volvemos a dejar la lista en tupla: {eighth_tuple}, {type(eighth_tuple)}")

#9. Elimina una tupla llamada my_tuple usando 'del' y luego intenta imprimirla para ver el resultado.
# Eliminate a tuple called my_tuple using 'del' and then try to print it to see the result.
my_tuple = (1, 3, 5, 7, 9)
print(f"Tupla: {my_tuple}")
del my_tuple
# print(my_tuple) -- NameError: name 'my_tuple' is not defined.
print(f"Despues de eliminar (my_tuple) con (del), al intentar imprimirla se genera el error: NameError: name 'my_tuple' is not defined.")

#10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
# Create a tuple with a single element (number 100) and print it. Be sure to use the correct syntax to create a tuple with a single element.
nineth_tuple = (100,)
print(f"Creamos la novena tubla: {nineth_tuple}")