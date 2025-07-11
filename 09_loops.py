        ### Loops ###
# 1. Use a while loop to print the numbers from 1 to 10
print("Imprimimos los números del 1 al 10.")
numbers = 1
while numbers <= 10:
    print(f"\t{numbers}")
    numbers += 1

# 2. Use a for loop to iterate the list [10, 20, 30, 40, 50] and print each number
print("\nImprimimos los numeros de la lista [10, 20, 30, 40, 50].")
first_list = [10, 20, 30, 40, 50]
for num_first_list in first_list:
    print(f"\t{num_first_list}")

# 3. Write a program that uses a while loop to sum the numbers from 1 to 100 and print the result
print("\nSumamos los números del 1 al 100.")
first_number = 1
sum_number = 0
while first_number <= 100:
    sum_number += first_number
    first_number +=1
print(f"\t{sum_number}")

# 4. Write a for loop that prints each character in the string "Python"
print("\nImprimimos cada caracter de la palabra 'Python'.")
word = 'Python'
for letter in word:
    print(f"\t{letter}")

# 5. Use a while loop to find the first number divisible by 7 between 1 and 50
print("\nBuscamos el primer número divisible de 7 entre 1 y 50.")
second_number = 1
while second_number <= 50:
    print(f"\t{second_number}")
    if second_number % 7 == 0:
        print(f"\tEl número {second_number} es divisible de 7.")
        break
    second_number += 1

# 6. Use a for loop to iterate through the dictionary {"name": "Brais", "age":37, "country":"Galicia"} and print the keys
print("\nImprimimos las claves del diccionario.")
first_dict = {"name":"Brais", "age":37, "country":"Galicia"}
for keys in  first_dict:
    print(f"\t{keys}")

# 7. Write a program that uses a while loop to print the even numbers between 1 and 20.
print("\nImprimimos los números pares entre 1 y 20.")
third_number = 1
while third_number <= 20:
    if third_number % 2 == 0:
        print(f"\t{third_number}")
    third_number += 1

# 8. Use a for loop with the range() function to print the numbers from 1 to 10 in reverse order.
print("\nImprimimos los números del 1 y 10 de orden inverso.")
for quarter_number in range(10, 0, -1):
    print(f"\t{quarter_number}")

# 9. Write a program that uses a for loop to count how many times the number 30 appears in the list [30, 10, 30, 20, 30, 40].
print("\nContamos el número 30 de la lista [30, 10, 30, 20, 30, 40].")
second_list = [30, 10, 30, 20, 30, 40]
count_number = 0
for num_second_list in second_list:
    if num_second_list == 30:
        count_number +=1
print(f"\tEl número 30 esta {count_number} veces.")

# 10. Use a for loop to iterate through a list of names and stop the loop when the name “Brais” is found.
print("\nDetenemos la busqueda en la lista ['Pedro', 'Juan', 'Brais', 'Jose', 'Albeiro'] cuando encuentre 'Brais'.")
names_list = ['Pedro', 'Juan', 'Brais', 'Jose', 'Albeiro']
for names in names_list:
    print(f"\t{names}")
    if names == 'Brais':
        print(f"\tEncontramos el nombre {names}")
        break

# Option 1 -Print number 1 at 10
number_a = 1
result_a = ""
while number_a <= 10:
    result_a += str(number_a) + ", "
    number_a += 1
print(f"({result_a[:-2]})")

# Option 2 -Print number 1 at 10
print(f"({', '.join(map(str, range(1, 11)))})")