        ### Operators ###

"""
#1. Realiza las siguientes operaciones aritméticas:
Suma: 15 + 25
Resta: 50 - 22
Multiplicación: 8 * 7
División: 100 / 20
"""
sum_number = 15 + 25
subtraction = 50 - 22
multiplication = 8 * 7
division = 100 / 20
print(f"Suma 15 + 25: {sum_number}")
print(f"Resta 50 - 22: {subtraction}")
print(f"Multiplicación 8 * 7: {multiplication}")
print(f"Division 100 / 20: {division}")

#2. Calcula el resto de la división de 37 entre 5 y almacénalo en una variable remainder. Luego imprímelo.
remainder = 37 % 5
print(f"Resto de la division 37 % 5: {remainder}")

#3. Convierte el número 7 en una cadena de texto y concaténalo con la frase “ es mi número favorito”. Imprime el resultado.
favorite_number = str(7)
print(f"{favorite_number} es mi numero favorito!!")

#4. Repite la palabra “Python” 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
word = "Python "
word_multiplication = word * 10
print(word_multiplication)

#5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si (a) es mayor que (b) y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8
print("a=12, b=8")
bool_result = a > b
print(f"a=12, b=8, comparación booleana a > b: {bool_result}")

#6. Compara dos cadenas de texto (“apple” y “banana”) usando los operadores > y < y explica cuál tiene mayor orden alfabético.
text_bigger = "banana" > "apple"
print(f"Comparación banana y apple: {text_bigger}")
"""
banana es mayor que apple, porque alfabéticamente esta comparación se realiza
carácter por carácter y b es mayo que a, de acuerdo al alfabeto.
"""

#7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.
first_comparison = (10>5)
second_comparison = (10<20)
result_comparison =first_comparison and second_comparison
print(f"Comparación lógica del número 10 que es mayor que 5 y menor 20: {result_comparison}")

#8. Usa el operador or para verificar si el número 7 es menor que 3 o mayor que 5. Imprime el resultado.
third_comparison = (7<3)
quarter_comparison = (7>5)
result_comparison_two = third_comparison or quarter_comparison
print(f"Comparación lógica del número 7 es menor que 3 o mayor que 5: {result_comparison_two}")

#9. Aplica el operador not para invertir el resultado de la comparación 15 > 20. ¿Cuál es el resultado?
comparison_not = not(15>20)
print(f"Operador not en comparación de 15>20: {comparison_not}")

#10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
exercise = ((5*3)+2 > 10) and ((5*3)+2 <20)
print(f"El número resultante de (5*3)+2 es mayor que 10 y menor que 20: {exercise}")

#Nota: Valores ASCII. - Note: Values ASCII.
print(ord("J"))  # 74
print(ord("u"))  # 117
print(ord("a"))  # 97
print(ord("n"))  # 110
