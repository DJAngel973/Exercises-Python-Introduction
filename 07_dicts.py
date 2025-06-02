        ### Dictionaries ###
# 1
first_dit = {
    "Name":"Pedro",
    "Age":30,
    "Country":"Colombia"
}
print(f"Creamos el primer diccionario:\n\t{first_dit}\n\t{type(first_dit)}")

# 2
print(f"Mostramos el valor de la clave Name:\n\t{first_dit['Name']}")

# 3
first_dit["Job"]="Programador"
print(f"Agregamos al diccionario la clabe job con el valor 'programador':\n\t{first_dit}")

# 4
first_dit["Age"] = 38
print(f"Modificamos el valor de la clave Age:\n\t{first_dit}")

# 5
del first_dit["Country"]
print(f"Eliminamos la clave Country:\n\t{first_dit}")

# 6
second_dit = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
print(f"Creamos un segundo diccionario:\n\t{second_dit}")

# 7
third_dit = {
    "name":"Brais",
    "age":37,
    "country":"Galicia"
}
print(f"Creamos el tecer diccionario:\n\t{third_dit}")
print(f"Verificamos que la clave age este en el tercer diccionario:\n\t{'age' in third_dit}")

# 8
print(f"Imprimimos solos las claves del tercer diccionario:\n\t{third_dit.keys()}")

# 9
new_list = list(third_dit.keys())
print(f"Convertimos las claves del tercer diccionario en una lista:\n\t{new_list}\n\t{type(new_list)}")

# 10
other_list = ["nombre", "age", "job"]
print(f"Creamos una otra lista:\n\t{other_list}\n\t{type(other_list)}")
quarter_dit = dict.fromkeys(other_list)
print(f"Creamos un diccionario apartir de la anterior lista:\n\t{quarter_dit}\n\t{type(quarter_dit)}")