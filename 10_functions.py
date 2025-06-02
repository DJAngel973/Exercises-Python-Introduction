        ### Functions ###
# 1
def personalized_greeting (name = "desconocido"):
    print(f"\nHola, {name}.")
personalized_greeting()

# 2
def multiply (first_number, second_number):
    return first_number * second_number
print(f"\nLa multiplicacion de 5 por 5 es: {multiply(5,5)}")

# 3
def is_even (third_number):
    return third_number % 2 == 0
print(f"\n¿El número 3 es par?: {is_even(3)}")

# 4
def convert_to_uppercase (string):
    return string.upper()
print(f"\n{convert_to_uppercase('Hoy es martes')}")

# 5
def arbitrary_sum (*numbers:int):
    sum_total = 0
    for number in numbers:
        sum_total += number
    return sum_total
print(f"\nLa suma de (14,45,85,12,40) es: {arbitrary_sum(14, 45, 85, 12, 40)}")

# 6
def generate_full_greeting (name="Nombre", last_name="Apellido"):
    return f"\nHola, {name} {last_name}."
print(generate_full_greeting())

# 7
def power (base, exponent):
    return base ** exponent
print(f"\nEl número 3 elevado a 5 es: {power(3, 5)}")

# 8
def calculate_average (first_number, second_number, third_number):
    return (first_number + second_number + third_number) / 3
print(f"\nEl promedio de 4, 5, 8 es: {calculate_average(4, 5, 8):.2f}")

# 9
def count_characters (string):
    return len(string)
print(f"\nLa cadena de texto 'Mas funciones' tien {count_characters('Mas funciones')} caracteres.")

# 10
def display_messages (*new_strings):
    print("")
    for new_string in new_strings:
        print(f"\t{new_string.upper()}")
display_messages("java", "python", "javascript", "c#")