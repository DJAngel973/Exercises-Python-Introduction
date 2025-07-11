        ### Conditionals ###
# 1. Write a program that checks if a number is positive, negative or zero
print("\nMiremos si un número es positivo, negativo o cero.")
number = int(input("\tPorfa escribe un número entero: "))
if number > 0:
    print(f"\t{number} es positivo.")
elif number < 0:
    print(f"\t{number} es negativo")
else:
    print(f"\t{number} es cero ")

# 2. Ask the user to enter their age and display a message indicating whether they are of legal age(18 years or older) or underage
age = int(input("\n¿Cuantos años tienes?(solo el número): "))
if age >= 18:
    print("\tEres mayor de edad.")
else:
    print("\tEres menor de edad.")

# 3. Write a program that checks if a text string is empty and displays a message accordingly
text = ""
if text:
    print(f"\nLa cadena de texto no esta vacia: {text}")
else:
    print(f"\nLa cadena de texto es vacia: {text}")

# 4. Create a program that asks the user for two numbers and compares which one is greater. if they are equal, display a message indicating the equality
print("\nComparemos dos números.")
first_number = int(input("\tPorfa ingresa el primer número: "))
second_number = int(input("\tAhora ingresa el segundo número: "))
if first_number > second_number:
    print(f"\t{first_number} es mayor que {second_number}.")
elif first_number < second_number:
    print(f"\t{second_number} es mayor que {first_number}.")
else:
    print(f"\tLos números {first_number} y {second_number} son iguales.")

# 5. Write a program that checks if a number is divisible by both 3 and 5 at the same time
print("\nVerifiquemos si un número es divisible por 3 y por 5 al mismo tiempo.")
third_number = int(input("\tIngresa un número: "))
if third_number % 3 == 0 and third_number % 5 == 0:
    print(f"\tEl {third_number} es divisible por 3 y por 5.")
else:
    print(f"\tEl {third_number} no es divisible por 3 y por 5 al mismo tiempo.")

# 6. Ask the user to enter a number and check whether it is even or odd
print("\nAhora verifiquemos si un número es par o impar")
quarter_number = int(input("\tIngresa un número: "))
if quarter_number % 2 == 0:
    print(f"\t{quarter_number} es par.")
else:
    print(f"\t{quarter_number} es impar.")

# 7. Write a program that determines whether a person can vote based on their age (18 or older). If they are 16 or 17, indicate that they can vote with special permission
print("\nMiremos si puedes ejercer el voto.")
age = int(input("\tPorfa ingresa tu edad: "))
if age >= 18:
    print(f"\tTienes {age} años, puedes ejercer el voto.")
elif 16 <= age < 18:
    print(f"\tTienes {age} años, puedes ejercer el voto con permiso especial.")
else:
    print(f"\tTienes {age} años, no puedes ejercer el voto.")

# 8. Create a program that asks the user for a password and checks whether it matches a predefined password. If it doesn't match, display an error message
print("\nVerifiquemos la contraseña predefinida")
password = "admin"
password_input = input("\tIngresa la contraseña: ")
if password_input == password:
    print("\tLa contraseña es correcta.")
else:
    print("\tLa contraseña es incorrecta.")

# 9. Write a program that determines if a number is between 10 and 20 (inclusive)
print("\nVerifiquemos un rango de número.")
fifth_number = int(input("\tIngresa un número: "))
if 10 <= fifth_number <= 20:
    print(f"\t{fifth_number} esta entre 10 y 20.")
else:
    print(f"\t{fifth_number} no esta entre 10 y 20.")

# 10. Write a program that simulates a traffic light: ask the user to ente e color (red, yellow, green)
# and display a message indicating whether they should stop, be alert, or go
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