        ### Classes ###
import math

# 1 y 2

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        if self.species == "Cow":
            print("\tMuu")
        elif self.species == "Cat":
            print("\tMiau")
        elif self.species == "Dog":
            print("\tGuau")
        else:
            print("\tSonido animal genérico.")

print("\nVerifiquemos algunos sonidos de animales.")
animal_a = Animal(input("\tPorfa ingresa un animal de estos Cow, Cat o Dog: "))
print(animal_a.make_sound())
animal_b = Animal(input("\tAhora ingresa un animal diferente, haber si encontramos algun sonido: "))
print(animal_b.make_sound())

# 3 y 4

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self._speed = speed

    def accelerate(self):
        self._speed += 10

    def brake(self):
        self._speed = max(0,self._speed - 10)

    def get_speed(self):
        return self._speed

print("\nMiremos un automovil andando.")
print("\tIngresa los siguientes datos: ")
car_one = Car(input("\tMarca: "), input("\tModelo: "))
print(f"\tEl {car_one.brand} del año {car_one.model}")
car_one.accelerate()
print(f"\tAumenta la velocidad en {car_one.get_speed()} unidades")
car_one.brake()
print(f"\tEl disminuye {car_one.get_speed()} km/h")

# 5
class Book:
    def __init__(self, title="público", author="privado"):
        self.title = title
        self.author = author

    def get_author(self):
        return print(f"\tEl autor es: {self.author}")

    def change_title(self, new_title):
        self.title = new_title

book_one = Book("El Principito", "Saint-Exupéry")
print(f"\nLibro: {book_one.title}")
print(f"\t{book_one.get_author()}")
print(f"\tNuevo libro: {book_one.change_title('El Universo')}")
print(f"\t{book_one.get_author()}")

# 6
class Estudiante:
    def __init__(self, name, lastname, grades):
        self.name = name
        self.lastname = lastname
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

print("\nSaquemos la media de tus notas.")
notas = input(f"\tIngresa las notas separas con una (,): ")
num_notas= list(map(int, notas.split(",")))
student = Estudiante(input("\tNombre: "), input("\tApellido: "), num_notas)
print(f"\tEl estudiante {student.name} {student.lastname}, tiene la nota media en: {student.average():.2f}.")

# 7
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if value <= self.balance:
            self.balance -= value
        else:
            print("\tFondos insuficientes.")

print(f"\nRealicemos un deposito y un retiro.")
user = input("\tNombre usuario: ")
user_balance = int(input("\tSaldo: "))
first_user = BankAccount(user, user_balance)
print(f"\tUsuario {first_user.owner}, Saldo {first_user.balance}")
user_deposit = int(input("\tIngresa el monto a depositar: "))
first_user.deposit(user_deposit)
print(f"\tDeposito {user_deposit}\n\t\tSaldo ${first_user.balance}")
user_withdraw =int(input("\tIngresa el monto a retirar: "))
first_user.withdraw(user_withdraw)
if user_withdraw < first_user.balance:
    print(f"\tRetiro {user_withdraw}\n\t\tSaldo ${first_user.balance}")

# 8
class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)

print("\nPorfa ingresa las coordenadas para allar la distancia entre dos puntos.")
first_point = Point(float(input("\tx1: ")), float(input("\ty1: ")), float(input("\tx2: ")), float(input("\ty2: ")))
print(f"\tLa distancia entre los dos puntos es: {first_point.distance():.2f}")

# 9
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.name = name
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def total_payment(self):
        return self.hourly_wage * self.hours_worked

print("\nCalculemos el total del pago con un sueldo de $14 por hora.")
name_employee = input("\t¿Como te llamas?: ")
employee_hourly_wage = 14
employee_hours_worked = int(input("\t¿Cuantas horas trabajaste? : "))
name_employee_payment = Employee(name_employee, employee_hourly_wage, employee_hours_worked)
print(f"\tEl valor total a pagar a {name_employee}, con {employee_hours_worked} horas trabajadas es de ${name_employee_payment.total_payment()}")

# 10
class Store:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add_up_inventory(self, product):
        self.inventory.append(product)

    def show_inventory(self):
        if not self.inventory:
            print("\tLa lista esta vacia.")
        else:
            print("\tProductos disponibles:", ", " .join(map(str, self.inventory)))

print("\nAgregemos algunas cosas al inventario.")
first_store = input("\tIngresa los datos separados por (,): ")
first_store_list= list(map(str, first_store.split(",")))
user_store = Store(first_store_list)
user_store.show_inventory()