        ### sets ###
# 1
first_set = {1, 2, 3, 4, 5}
print(f"Creamos un primer set: {first_set}, {type(first_set)}")

# 2
first_set.add(6)
print(f"Añadimos el número 6 al set: {first_set}")

# 3
first_set.add(5)
print(f"Añadimos el número 5 al set: {first_set}, no se agrega porque un set no permite datos repetidos.")

# 4
print(f"Verificamos si el número 3 esta en el set: {3 in first_set}")

# 5
first_set.remove(4)
print(f"Eliminamos el número 4 del set: {first_set}")

# 6
first_set.clear()
print(f"Limpiamos el set: {first_set}, quedando con una longitud de: {len(first_set)}")

# 7
second_set = {"manzana", "naranja", "plátano"}
print(f"Creamos el segundo set: {second_set}, {type(second_set)}")
second_set = list(second_set)
print(f"Convertimos el segundo set en una lista: {second_set}, {type(second_set)}")
print(f"Mostramos el primer el elemento de la lista: {second_set[0]}")

# 8
third_set = {1, 2, 3}
quarter_set = {4, 5, 6}
print(f"Creamos el tercer y cuarto set: {third_set} {quarter_set}")
union_set = third_set.union(quarter_set)
print(f"Unimos el tercer  y cuarto set: {union_set}")

# 9
fifth_set = {1, 2, 3, 4}
sixth_set = {3, 4, 5, 6}
set_difference = fifth_set.difference(sixth_set)
print(f"Creamos el quinto set {fifth_set} y el sexto set {sixth_set}, calculamos la diferencia entre estos dos set: {set_difference}")

# 10
my_set = {"a", "b"}
print(f"Creamos my_set: {my_set}")
del my_set
# del elimina, por imprimir my set, se genera el error: NameError: name 'my_set' is not defined