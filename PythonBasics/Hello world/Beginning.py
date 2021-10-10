# import math

# print('Zaid Mujahid')
# print('o---')
# print(' ||||')
# print('*' * 10)
# full_name = 'John Smith'
# age = 20
# is_new = True
# print(full_name, age, is_new)
#
# name = input('What is your name? ')
# color = input('What is your fav colour? ')
# print(name + ' likes ' + color)

# pounds = input('Input your weight(lbs): ')
# kilograms = float(pounds) * 0.45
# print(kilograms)
# strings can be defined either with double quotes or single quotes also
# course = "Python's course for beginners"
# print(course)
# subject = 'Python course for "beginners"'
# print(subject)
# #for very long strings
# email = '''
# Hi Zaid,
# Here is our first email for you.
# Thank you,
# The support team
# '''
# print(email)
# course = "Python's course for beginners"
# print(course[0])
# print(course[-1])
# print(course[-2])
# print(course[0:3])
# print(course[0:])
# print(course[1:5])
# print(course[:5])
# print(course[0:-3])
# print(course[:])
#
# #formatted strings
# first = "Zaid"
# last = "Mujahid"
# message = first + ' [' + last + '] is a coder'
# print(message)
# msg = f'{first} [{last}] is a coder'
# print(msg)

# course = "Python's course for beginners"
# print(len(course))
# print(course.upper())#it creates a new string for storing upper case
# print(course)
# print(course.find('o'))
# print(course.find('for'))
# print(course.replace('Beginners', 'Absolute beginners'))
# print('Python' in course)#to check existence of a char or word it is a boolean value
# print(course.title())#dont know what it does

# operators in py
# print(19 + 4)
# print(19 - 4)
# print(19 * 4)
# print(19 / 4)
# print(19 // 4)#only int value
# print(19 % 4)
# print(19 ** 4)#power operator
# operator precedence
# parenthesis > exponenciation > multi or div > add or sub

# some math functions
# x = 2.6
# print(round(x))
# print(abs(x))
#
# print(math.ceil(x))
# print(math.floor(x))
# go to python 3 math module on browser and learn other functions
# if statements
# price = 100000
# good_credit = False
# if good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")

# weight converter
# while loop
# i = 1
# while i<=5:
#     print('*' * i)
#     i += 1
# print('Great Pattern!')
# No. guessing game
# target = 8
# chances = 0
# while chances < 3:
#     guess = int(input('Guess the number: '))
#     chances += 1
#     if guess == target:
#         print("Correct guess!")
#         break
# else:
#     print("You dumbass!")
# get_started = ""
# started = False
# while True:
#     get_started = input("> ").lower()
#     if get_started == "start":
#         if started:
#             print("Car is already started!")
#         else:
#             started = True
#             print("Car started")
#     elif get_started == "end":
#         if not started:
#             print("Car is already stopped!")
#         else:
#             started = False
#             print("Car stopped")
#     elif get_started == "help":
#         print('''
# Start - to start the car
# End - to stop the car
# Exit - to quit the game''')
#     elif get_started == "quit":
#         break
#     else:
#         print("I don't understand")
# for loop
# numbers = [1, 1, 1, 1, 5]
# for i in numbers:
#     output = ''
#     for j in range(i):
#         output += 'x '
#     print(output)

# lists
# It will also create new list to store modified values
# names = ['Zaid', 'Umair', 'Anas', 'Farhan']
# print(names[-2])
# print(names[0])
# print(names[0:3])
# print(names[:])
# print(names[2:-2])
# print(names[0:-2])
# print(names[2:])
# names[0] = 'Zaid Mujahid'
# print(names)
# 2D lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in matrix:
#     for j in i:
#         print(j)
# numbers = [3, 4, 6, 4, 9, 8]
# numbers.append(34)
# print(numbers)
# numbers.insert(0,18)
# numbers.remove(4)
# numbers.pop()
# print(numbers)
# # numbers.clear()
# numbers.index(6)
# print(50 in numbers)
# print(8 in numbers)
# print(numbers.count(4))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(3)
# print(numbers)
# print(numbers2)

# unique = []
# for i in numbers:
#     if i not in unique:
#         unique.append(i)
# print(unique)
# tuples
# number = (1, 3, 5)
# #only two methods
# print(number[0])
# cannot change value

# Unpacking
# coordinates = (1, 2, 3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# instead of this we can use unpacking
# x, y, z = coordinates
# print(x)
# print(y)
# print(z)
# # Dictionaries

# customer = {
#     "name": "Farhan",
#     "age": 23,
#     "is_verified": True
#     }
# print(customer["name"])
# print(customer.get("birthdate", "Jan 12 2020"))
# default value if the value is not there
# customer["name"] = "Zaid"
# print(customer["name"])
# customer["birthdate"] = "27-4-2002"
# print(customer)
# problem
# Phone = input("Phone: ")
# phone = {
#     "1": "one",
#     "2": "two",
#     "3": "three"
# }
# output = ""
# for i in Phone:
#     output += phone.get(i, "!") + " "
# print(output)

# Emojiconverter
# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)": "😁😍",
#     ":(": "😥"
# }
# output = ""
# for i in message:
#     output += emojis.get(i, i)
# print(output)

# Functions
# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome abroad")
#
#
# greet_user("Zaid", "Mujahid")
#
# def square(num):
#     return num * num
#
#
# print(square(4))
#
# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😁",
#          ":(": "😥"
#     }
#     output = ""
#     for i in message:
#            output += emojis.get(i, i) + ""
#     return output
#
# message = input(">")
# print(emoji_converter(message))

# Exceptions
# try:
#     age = int(input("Age: "))
#     print(f"Your Age is {age}")
# except ValueError:
#     print("Invalid value")

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income/age
#     print(f"Your Age is {age}")
# except ZeroDivisionError:
#     print("Age cannot be zero")

# classes
# class Point:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
#
# point1 = Point()
# point1.draw()
# point1.x = 10
# point1.y = 20
# print(point1.x)
#
# point2 = Point()
# point2.x = 3
# print(point2.x)
# Constructors
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point = Point(10, 20)
# point.x = 11
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# john = Person("John Smith")
# john.talk()
#
# bob = Person("Bob Smith")
# bob.talk()

# Inheritance
# instead of defining dog and cat separately we can define another class to use in both
# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     # pass instead of empty body we are writing pass it does nothing
#         def bark(self):
#             print("bark")
#
#
# class Cat(Mammal):
#     # pass
#     def annoying(self):
#         print("annoying")
#
#
# # dog1 = Dog()
# # dog1.walk()
#
# cat1 = Cat()
# cat1.annoying()


# accessing packages

# import Ecommerce.shipping
# Ecommerce.shipping.cal_shipping()

# from Ecommerce.shipping import cal_shipping
# cal_shipping()

# from Ecommerce import shipping
# shipping.cal_shipping()

# Generating random values using inbuilt modules
import random


# print(random.random())  # random value bet 0 to 1
# print((random.randint(1, 100)))
#
# members = ['Zaid', 'Muzammil', 'Aum']
# leader = random.choice(members)
# print(leader)

# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second  # to return tuple it's not necessary to add parenthesis
#
#
# dice = Dice()
# print(dice.roll())


#working with directories
from pathlib import Path

# path = Path("Ecommerce")
# print(path.exists())
# path = Path("Ecommedrce")
# print(path.exists())
# # path = Path("emails")
# # print(path.mkdir())
# path = Path("emails")
# print(path.rmdir())

path = Path()
for file in path.glob('*'):
    print(file)











