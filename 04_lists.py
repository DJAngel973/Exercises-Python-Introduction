        ### lists ###
# 1
my_list_number = [1, 2, 3, 4, 5]
print(f"Lista de números: {my_list_number}")
print(type(my_list_number))

# 2
list_one = [10, 20, 30, 40, 50]
print(f"lista uno: {list_one}")
print(f"Mostramos el número de la tercera posicion de la lista uno: {list_one[2]}")

# 3
my_list_number.append(6)
print(f"Agregamos el número 6 a la lista de números: {my_list_number}")

# 4
list_one.insert(2, 15)
print(f"Insertamos el número 15 en la primera posicion en la lista uno: {list_one}")

# 5
list_two = [10, 20, 30, 30, 40, 50]
print(f"Lista dos: {list_two}")
list_two.remove(30)
print(f"Eliminamos el primer valor 30 de la lista dos: {list_two}")

# 6
my_list_pop = my_list_number.pop()
print(f"Lista de números ya sin el ultimo número eliminado por el pop: {my_list_number}")
print(f"El número que elimina pop, se guarda en una lista pop: {my_list_pop}")

# 7
list_three = [100, 200, 300, 400, 500]
print(f"Lista tres: {list_three}")
list_three.reverse()
print(f"Invertimos la lista tres con reverse: {list_three}")

# 8
list_four = [3, 1, 4, 2, 5]
print(f"Lista cuatro: {list_four}")
list_four.sort()
print(f"Odenamos la lista cuatro de forma ascendente con sort: {list_four}")

# 9
list_five = [1, 2, 3]
print(f"Lista cinco: {list_five}")
list_six = [4, 5, 6]
print(f"Lista seis: {list_six}")
list_five_and_six = list_five + list_six
print(f"Concatenamos las lista cinco y seis: {list_five_and_six}")

# 10
print(f"Recordamos la list dos: {list_two}")
print(f"Creamos una sublista de la lista dos, desde la posicion 1 a la 3, sin mostrar la #3: {list_two[1:3]}")