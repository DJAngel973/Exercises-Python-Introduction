        ### Variables ###
# 1
name = "Pedro"
age = 30
height = 1.80
print(f"My name is: {name}")
print(f"My age is: {age} years")
print(f"My height is: {height} mts")

# 2
age_str = str(age)
print(f"Im  {age_str} years old.")
print(type(age_str))

# 3
is_student = True
print(f"{name} is student: {is_student}")
if is_student:
    print(f"{name} is student.")
else:
    print(f"{name} is not a student.")

# 4
print(len(name))
print(f"The number of characters in your name are: {len(name)}")

# 5
first_name, las_name, city = "Juan David", "Angel", "Bogota"
print(f"Hello, Im {first_name} {las_name} from {city}.")

# 6
color = input("What is your favorite color? ")
print(f"{first_name} your favorite color is: {color}")

# 7
fruit = "apple"
print(fruit)
fruit = "pear"
print(fruit)

# 8
price = 8.3
print(price)
print(type(price))
price = int(8.3)
print(price)
print(type(price))

# 9
address = "Calle 124 # 15-42"
print(f"Address: {address}")
address_len = len(address)
print(f"Number of characters the address is: {address_len}")

# 10
phone = int(300872059418)
print(f"First phone: {phone}")
phone = 301974358475
print(f"Second phone: {phone}")
print(type(phone))