        ### Conditionals ###
# 1
print("\nMiremos si un número es positivo, negativo o cero.")
number = int(input("\tPorfa escribe un número entero: "))
if number > 0:
    print(f"\t{number} es positivo.")
elif number < 0:
    print(f"\t{number} es negativo")
else:
    print(f"\t{number} es cero ")

# 2
age = int(input("\n¿Cuantos años tienes?(solo el número): "))
if age >= 18:
    print("\tEres mayor de edad.")
else:
    print("\tEres menor de edad.")

# 3
text = ""
if text:
    print(f"\nLa cadena de texto no esta vacia: {text}")
else:
    print(f"\nLa cadena de texto es vacia: {text}")

# 4
print("\nComparemos dos números.")
first_number = int(input("\tPorfa ingresa el primer número: "))
second_number = int(input("\tAhora ingresa el segundo número: "))
if first_number > second_number:
    print(f"\t{first_number} es mayor que {second_number}.")
elif first_number < second_number:
    print(f"\t{second_number} es mayor que {first_number}.")
else:
    print(f"\tLos números {first_number} y {second_number} son iguales.")

# 5
print("\nVerifiquemos si un número es divisible por 3 y por 5 al mismo tiempo.")
third_number = int(input("\tIngresa un número: "))
if third_number % 3 == 0 and third_number % 5 == 0:
    print(f"\tEl {third_number} es divisible por 3 y por 5.")
else:
    print(f"\tEl {third_number} no es divisible por 3 y por 5 al mismo tiempo.")

# 6
print("\nAhora verifiquemos si un número es par o impar")
quarter_number = int(input("\tIngresa un número: "))
if quarter_number % 2 == 0:
    print(f"\t{quarter_number} es par.")
else:
    print(f"\t{quarter_number} es impar.")

# 7
print("\nMiremos si puedes ejercer el voto.")
age = int(input("\tPorfa ingresa tu edad: "))
if age >= 18:
    print(f"\tTienes {age} años, puedes ejercer el voto.")
elif 16 <= age < 18:
    print(f"\tTienes {age} años, puedes ejercer el voto con permiso especial.")
else:
    print(f"\tTienes {age} años, no puedes ejercer el voto.")

# 8
print("\nVerifiquemos la contraseña predefinida")
password = "admin"
password_input = input("\tIngresa la contraseña: ")
if password_input == password:
    print("\tLa contraseña es correcta.")
else:
    print("\tLa contraseña es incorrecta.")

# 9
print("\nVerifiquemos un rango de número.")
fifth_number = int(input("\tIngresa un número: "))
if 10 <= fifth_number <= 20:
    print(f"\t{fifth_number} esta entre 10 y 20.")
else:
    print(f"\t{fifth_number} no esta entre 10 y 20.")

# 10
print("\nSemáforo.")
traffic_light = input("\tIngresa un color (rojo, amarillo o verde). ")
if traffic_light == "rojo":
    print("\tParar.")
elif traffic_light == "amarillo":
    print("\tEstar alerta.")
elif traffic_light == "verde":
    print("\tAvanzar.")
else:
    print(f"\tLa palabra {traffic_light} es incorrecta, debe ser (rojo, amarillo o verde)")