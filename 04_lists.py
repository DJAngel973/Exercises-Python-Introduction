        ### lists ###
#1. Crea una lista con los números del 1 al 5 e imprímela. -Create a list with the numbers from 1 to 5 and print it.
my_list_number = [1, 2, 3, 4, 5]
print(f"Lista de números: {my_list_number}")
print(type(my_list_number))

#2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50]. -Access and print the third element of the list [10, 20, 30, 40, 50].
list_one = [10, 20, 30, 40, 50]
print(f"lista uno: {list_one}")
print(f"Mostramos el número de la tercera posición de la lista uno: {list_one[2]}")

#3. Agrega le número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela. -Add the number 6 to the end of the list [1, 2, 3, 4, 5] and print it.
my_list_number.append(6)
print(f"Agregamos el número 6 a la lista de números: {my_list_number}")

#4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50]. -Insert the number 15 at position 2 of the list [10, 20, 30, 40, 50].
list_one.insert(2, 15)
print(f"Insertamos el número 15 en la primera posición en la lista uno: {list_one}")

#5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50]. -Removes the first value 30 from the list [10, 20, 30, 30, 40, 50]
list_two = [10, 20, 30, 30, 40, 50]
print(f"Lista dos: {list_two}")
list_two.remove(30)
print(f"Eliminamos el primer valor 30 de la lista dos: {list_two}")

#6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable, imprime la variable y la lista.
# Use the pop() to remove the last element from list [1, 2, 3, 4, 5] and store it in a variable, print the variable and the list.
my_list_pop = my_list_number.pop()
print(f"Lista de números ya sin el ultimo número eliminado por el pop: {my_list_number}")
print(f"El número que elimina pop, se guarda en una lista pop: {my_list_pop}")

#7. Invierte la lista [100, 200, 300, 400, 500] e imprímela. -Reverse the list [100, 200, 300, 400, 500] and print it.
list_three = [100, 200, 300, 400, 500]
print(f"Lista tres: {list_three}")
list_three.reverse()
print(f"Invertimos la lista tres con reverse: {list_three}")

#8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela. -Sort the list [3, 1, 4, 2, 5] in ascending order and print it.
list_four = [3, 1, 4, 2, 5]
print(f"Lista cuatro: {list_four}")
list_four.sort()
print(f"Ordenamos la lista cuatro de forma ascendente con sort: {list_four}")

#9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
# Concatenates the lists [1, 2, 3] and [4, 5, 6] and stores the result in a new list. Prints the resulting list.
list_five = [1, 2, 3]
print(f"Lista cinco: {list_five}")
list_six = [4, 5, 6]
print(f"Lista seis: {list_six}")
list_five_and_six = list_five + list_six
print(f"Concatenamos las lista cinco y seis: {list_five_and_six}")

#10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
# Create a sublist with the elements of the list [10, 20, 30, 40, 50] ranging from the position 1 to 3 (not including position 3).
print(f"Recordamos la list dos: {list_two}")
print(f"Creamos una sublista de la lista dos, desde la posicion 1 a la 3, sin mostrar la #3: {list_two[1:3]}")