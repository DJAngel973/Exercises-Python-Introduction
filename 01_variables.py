        ### Variables ###

"""
1. Declara y asigna valores a las siguientes variables:
name: una cadena que contenga tu nombre.
age: un número entero que represente tu edad.
height: un número flotante que represente tu altura.
Imprime cada variable en una línea separada.
"""
name = "Pedro"
age = 30
height = 1.80
print(f"My name is: {name}")
print(f"My age is: {age} years")
print(f"My height is: {height} mts")

#2. Convierte la variable edad de entero a cadena y concaténala con un texto que diga cuántos años tienes.
age_str = str(age)
print(f"Im  {age_str} years old.")
print(type(age_str))

#3. Declara una variable booleana is_student que indique si eres estudiante o no. Usa True o False según corresponda e imprímela.
is_student = True
print(f"{name} is student: {is_student}")
if is_student:
    print(f"{name} is student.")
else:
    print(f"{name} is not a student.")

#4. Usa la función len() para calcular cuántos caracteres tiene tu nombre completo, almacenado en una variable.
print(len(name))
print(f"The number of characters in your name are: {len(name)}")

#5. Declara tres variables en una sola línea que representen tu nombre, apellido y ciudad de origen. Luego, imprime estos valores.
first_name, las_name, city = "Juan David", "Angel", "Bogota"
print(f"Hello, Im {first_name} {las_name} from {city}.")

#6. Usa la función input() para solicitar al usuario su color favorito y almacénalo en variable color. Luego, imprime el valor ingresado.
color = input("What is your favorite color? ")
print(f"{first_name} your favorite color is: {color}")

#7. Declara una variable fruit e inicialízala con un valor. Luego, cambia el valor de la fruta a otro diferente y vuelve a imprimirla.
fruit = "apple"
print(fruit)
fruit = "pear"
print(fruit)

#8. Convierte un número decimal, almacenado en la variable price, a un número entero y luego imprímelo.
price = 8.3
print(price)
print(type(price))
price = int(8.3)
print(price)
print(type(price))

#9. Declara una variable llamada address_len y almacena en ella la cantidad de caracteres de una dirección usando la función len(). Imprime el resultado.
address = "Calle 124 # 15-42"
print(f"Address: {address}")
address_len = len(address)
print(f"Number of characters the address is: {address_len}")

#10. Usa un tipo de dato forzado para declarar una variable phone, asegurándote de que siempre será un número. Luego, cambia su valor a un número diferente y verifica el tipo de la variable con type().
phone = int(300872059418)
print(f"First phone: {phone}")
phone = 301974358475
print(f"Second phone: {phone}")
print(type(phone))