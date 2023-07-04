print("Hello World 🤣")
print("*"*10)

# variables
y = 2
x = 1

rating = 4.99
is_published = True

course_name = """
STAT________long string
616
"""
print(course_name)


x = 1
y = 2
x, y = 1, 2
x = y = 1

x = [1, 2, 3]
print(type(x))
print(x[-1])
len(x)

course = "stat 616"
print(course)
print(course[-2])
print(course[0:3])
print(course.upper())
print(course.title())
print(course.find("tat"))
print("stat" in course)


# arithmetics
x = 6.0/5
round(x) # built-in functions
x = 2**3
# math module
import math
age=22.3
math.floor(age)

# if... else...
age = 2
if age >= 18: 
    print("Adult")
elif age >=13:
    print("Teenager")
else:
    print("Child")

# loops
x1, x2 = 0, 1
for i in range(10):
    if i==0:
        print(x1)
        print(x2)
    x3 = x1+x2
    x1 = x2
    x2 = x3
    print(x2)


n = int(input("number of iterations: "))
i = 1
x1, x2 = 0, 1
while True:
    x3 = x1+x2
    x1 = x2
    x2 = x3
    print(x2)
    i += 1
    if i>n:
        break


names = ["Hannah","John", "Mary", "Wei"]
flg = False
for name in names:
    if name.startswith("J"):
        flg = True
        print("Found")
        break
if not flg: 
    print("Not Found")


# functions
def increment(number, by=1):
    return number+by

increment(2,by=3)
increment(2)


# list
names = ['John','Bob','Sarah','Wei']
print(names[0:2])
print(names[2:])
names[0] = 'Jon'

names1 = ('John','Bob','Sarah','Wei') #tuple
names1[0] = 'Jon'

numbers = [3,2,5]

def fibonacci(n):
    x = [0,1]
    for i in range(n):
        x.append(x[i]+x[i+1]) # list method
    return x

fib = fibonacci(10)
print(fib)

a = [[1,2],[2,4,5],["John","Bob"]]

# 2D list / matrix
mat = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat[0][1])

import numpy as np
mat1 = np.array(mat)
mat1[0,1]

for row in mat:
    for num in row:
        print(num)



# dictionary
student = {
    "name": "No One",
    "ID": 12345,
    "is_registered": True
}
student.get("name")
student.get("age","NA")
student["age"] = 50
student.get("age","NA")
student["age"]

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😁",
        ":(": "😣"
    }
    temp = ""
    for word in words:
        temp = temp+emojis.get(word,word)+" "
    return temp

emoji_converter(input('say something?\n'))


# module
import converters
print(converters.lbs_to_kg(70))

from converters import lbs_to_kg  # or from package import module
print(lbs_to_kg(70))


# generating random numbers
import random
for i in range(3):
    random.random()

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second

dice = Dice()
print(dice.roll())


# classes
class Point:
    def __init__(self, x, y): #constructor
        self.x = x
        self.y = y

    def print_loc(self):
        print(f"Point location is x = {self.x}, y = {self.y}")

    def sum(self):
        return self.x+self.y

    def product(self):
        return self.x*self.y
        

point1 = Point(5,10)
point1.print_loc()
point1.sum()

# class inheritance

class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def crawl(self):
        print("crawl")

x = Dog()
x.walk()
x.bark()
y = Cat()
x.walk()
y.crawl()


