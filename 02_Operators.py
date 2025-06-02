        ### Operators ###
# 1
print(f"Suma 15 + 25: {15+25}")
print(f"Resta 50 - 22: {50-22}")
print(f"Multiplicación 8 * 7: {8*7}")
print(f"Division 100 / 20: {100/20}")

# 2
remainder = 37 % 5
print(f"Resto de la division 37 % 5: {remainder}")

# 3
favorite_number = str(7)
print(f"{favorite_number} es mi numero favorito!!")

# 4
word = "Python "
print(word * 10)

# 5
a = 12
b = 8
print(f"a=12, b=8")
bool_result = a > b
print(f"a=12, b=8, comparación booleana a > b: {bool_result}")

# 6
text_bigger = "banana" > "apple"
print(f"Comparación banana y apple: {text_bigger}")
"""
banana es mayor que apple, porque alfabeticamente esta comparacion se realiza
caracter por caracter y b es mayo que a, de acuerdo al alfabeto.
"""

# 7
print(f"Comparación lógica del número 10 que es mayor que 5 y menor 20: {(10>5) and (10<20)}")

# 8
print(f"Comparción lógica del número 7 es menor que 3 o mayor que 5: {(7<3) or (7>5)}")

# 9
print(f"Operador not en comparacion de 15>20: {not(15>20)}")

#10
print(f"El número resultante de (5*3)+2 es mayor que 10 y menor que 20: {((5*3)+2 > 10) and ((5*3)+2 <20)}")

# Valores ASCII. - Values ASCII.
print(ord("J"))  # 74
print(ord("u"))  # 117
print(ord("a"))  # 97
print(ord("n"))  # 110
