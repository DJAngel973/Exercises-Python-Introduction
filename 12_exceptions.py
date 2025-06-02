        ### Exception Handling ###
import math

# 1
def divided_numbers(number_one, number_two):
    return number_one / number_two

print("\n#1 Realicemos una pequeña division.")

try:
    numbers_user = divided_numbers(int(input("\tIngresa el primer número: ")), int(input("\tIngresa el segundo número: ")))
    print(f"\tEl resultado es: {numbers_user:.2f}")
except ValueError as error:
    print(f"\tError, debes ingresar un número entero. ({error})")
except ZeroDivisionError as error:
    print(f"\tError, no se puede devidir por cero. ({error})")

# 2
def one_int(int_one):
    return int(int_one)

print("\n#2 Ingresa una cadena e intentamos pasarla a entero.")

try:
    first_int = one_int(input("Ingresa un valor: "))
    print(f"Ingresaste: {first_int}")
except Exception as error_one_int:
    print(f"\tError: {error_one_int}")

# 3
def archive(file_one):
    try:
        with open(file_one, "r") as file:
            archive_one = file.read()
            return archive_one
    except FileNotFoundError as error_file_not:
        return f"\tError, no se encontro el archivo, tipo error:({error_file_not})"
    except PermissionError as error_permits:
        return f"\tError, archivo sin permiso de lectura. tipo error:{error_permits}"
    except Exception as e:
        return f"\tError: {e}"

print("\n#3 Intentemos abrir un archivo y leerlo.")
user_archive = archive(input("Ingresa un archivo: "))
if "Error" not in user_archive:
    print(f"\tlectura archivo: {user_archive}.")
else:
    print(f"\t{user_archive}")

# 4
print("\n#4 Realizemos algunas operaciones.")

def operations(number_one, number_two):
    try:
        addition = number_one + number_two
        subtraction = number_one - number_two
        multiplication = number_one * number_two
        division = number_one / number_two
    except ZeroDivisionError as error_zero:
        return f"\tError, no se puede devidir por cero. ({error_zero})"
    except Exception as error_operations:
        return f"\tError: {error_operations}"
    else:
        return addition, subtraction, multiplication, division
    finally:
        print("\tContinuamos con la ejecución.")

try:
    first_number = int(input("\tEscribe el primer número: "))
    second_number = int(input("\tEscribe el segundo número: "))
    results = operations(first_number, second_number)
except ValueError as error_value_rusults:
    print(f"\tError,  debes ingresar un número entero. ({error_value_rusults})")
except Exception as error_type:
    print(f"\tError: {error_type}")
else:
    if isinstance(results, tuple):
        add_result, sub_result, mul_result, div_result = results
        print(f"\tLas operaciones de {first_number} y {second_number}")
        print(f"\tSuma: {add_result}")
        print(f"\tResta: {sub_result}")
        print(f"\tMultiplicación: {mul_result}")
        print(f"\tDivisión: {div_result:.2f}")
    else:
        print(results)

# 5
def user_age(age):
    if age < 0:
        raise ValueError ("\tLa edad no puede ser un número negativo.")
    return age

try:
    user_one = user_age(int(input("\n#5 Ingresa tu edad: ")))
    print(f"\tTienes {user_one} años.")
except ValueError as error_value_user_age:
    print(f"\tError, la edad no es acorde a un entero positivo: {error_value_user_age}")
except Exception as error_exception_age:
    print(f"\tError: {error_exception_age}")

# 6
print("\n#6 Busquemos un elemento de la lista mediante el indice.")
def list_element(one_lista, index_element):
    try:
        return one_lista[index_element]
    except IndexError as error_index_list:
        return f"\tError, ingresaste un indice fuera de rango, tipo error: {error_index_list}."
    except Exception as error_list_element:
        return f"\tError: {error_list_element}"

try:
    user_input_list = input("\tIngresa algunas elementos a la lista, separados por (,): ")
    user_list = [item.strip() for item  in user_input_list.split(",")]
    index_user_list = int(input(f"\tIngresa el numero del indice de la lista que quieres mirar: "))
    element_index = list_element(user_list, index_user_list)
except Exception as e_general:
    print(f"Error: {e_general}.")
else:
    if isinstance(element_index, str) and element_index.startswith("\tError,"):
        print(element_index)
    else:
        print(f"\tLista: {user_list}")
        print(f"\tEl indice {index_user_list} tiene el elemento: {element_index}")

# 7
def exceptions(first_num, second_num):
    try:
        result_division = first_num / second_num
        return f"\tLa divison de {first_num} y {second_num} es: {result_division:.2f}, no hubo errores."
    except TypeError:
        return f"\tError, el tipo de dato no concuerda con la operación."
    except ValueError:
        return f"\tError,  debes ingresar un valor correcto."
    except ZeroDivisionError:
        return f"\tError, no se puede dvividr por cero."
    except Exception as error_exceptions:
        return f"\tError inesperado, tipo: {error_exceptions}"
try:
    print("\n#7 problemos algunos errores con una división.")
    number_1 = int(input("\tIngres un número entero: "))
    number_2 = int(input("\tIngresa otro número entero: "))
    test_exceptions = exceptions(number_1, number_2)
    print(test_exceptions)
except Exception as error_test:
    print(f"\tError, tipo: {error_test}.")

# 8
class InsufficientFundsError(Exception):
    pass

def transactions(balance, deposit, withdraw):
    try:
        initial_balance = balance
        balance_sum = initial_balance + deposit
        if balance_sum < withdraw:
            raise InsufficientFundsError(f"Fondos insuficientes.")
        final_balance = balance_sum - withdraw
        return balance_sum, final_balance
    except InsufficientFundsError as error_funds_transaction:
        return f"\tError, {error_funds_transaction}"
    except Exception as error_transaction:
        return f"\tError, tipo: {error_transaction}."

print("\n#8 Realisemos una transaccion.")
try:
    user_balance = int(input("\tSaldo actual?: "))
    user_deposit = int(input("\tIngresa el valor a depositar: "))
    user_withdraw = int(input("\tIngresa el valor a retirar: "))
    user_one_transactions = transactions(user_balance, user_deposit, user_withdraw)
    if isinstance(user_one_transactions, tuple):
        balance_sum_calc, final_balance_calc = user_one_transactions
        print(f"\tSaldo: {user_balance}")
        print(f"\tSaldo con deposito: ${balance_sum_calc}")
        print(f"\tSaldo final con retiro: ${final_balance_calc}")
    else:
        print(user_one_transactions)
except ValueError:
    print("\tError, no ingresaste un número valido.")
except Exception as user_error_general:
    print(f"\tError, tipo: {user_error_general}.")

# 9
def convert_list(string_list: list):
    try:
        int_list = [int(value.strip()) for value in string_list]
        return int_list
    except ValueError:
        return f"\tError, uno o mas valores no son número enteros validos."
    except Exception as error_convert:
        return f"\tError inesperado, tipo: {error_convert}"

try:
    print("\n#9 Convirtamos una lista string a int.")
    input_str = input("\tIngresa algunos valores a la lista separados con (,): ")
    string_elements_list = [item.strip() for item in input_str.split(",")]
    now_list = convert_list(string_elements_list)
    if isinstance(now_list, list):
        print(f"\tLa lista de números enteros es: {now_list}")
    else:
        print(now_list)
except Exception as error_general_list:
    print(f"\tError, inesperado tipo: {error_general_list}.")

# 10
def square_root(number):
    try:
        return math.sqrt(number)
    except ValueError:
        return f"\tError el número es negativo, no se puede calcular la raiz cuadrada."

try:
    print("\n#10 Relicemos una raiz cuadrada.")
    number_user = int(input("\tIngresa un número entero: "))
    result_number_user = square_root(number_user)
    if isinstance(result_number_user, (int, float)):
        print(f"\tLa raiz cuadrada de {number_user} es: {result_number_user:.2f}.")
    else:
        print(result_number_user)
except ValueError:
    print("\tError, no ingresaste un número entero valido.")
except Exception as e_number:
    print(f"\tError, inesperado tipo: {e_number}.")