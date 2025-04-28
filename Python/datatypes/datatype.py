#getting the type of var
#string
x = "mrng"
print(x)
print(type(x),"\n")

#integer
x = 5 
print(x)
print(type(x),"\n")

#boolean
x = True 
print(x)
print(type(x),"\n")

#float
x = 20.0 
print(x)
print(type(x),"\n")

#complex
x = 1j 
print(x)
print(type(x),"\n")

#list
x = ["apple", "banana", "cherry"]
print(x)
print(type(x),"\n")

#tuple
x = ("apple", "banana", "cherry")
print(x)
print(type(x),"\n")

#range
x = range(5)
print(x)
print(type(x),"\n")

#dict
x = {"name" : "John", "age" : 24}
print(x)
print(type(x),"\n")

#set
x = {"apple", "banana", "cherry"}
print(x)
print(type(x),"\n")

#bytes
x = b"hello"
print(x)
print(type(x),"\n")

#memory
x = memoryview(bytes(5))
print(x)
print(type(x),"\n")

#setting data type
#
x = list(("apple", "banana", "cherry"))
print(x)
print(type(x),"\n")

#string
x = str("hello")
print(x)
print(type(x),"\n")

#set
x = set(("apple", "banana", "cherry"))
print(x)
print(type(x),"\n")

#dict
x = dict(name='jenny',age=28)
print(x)
print(type(x),"\n")

#bool
x = bool(5)
print(x)
print(type(x),"\n")

#float
x = float(20.6)
print(x)
print(type(x),"\n")

#python variables
x = 1
y = 1.2
z = 1j
print(type(x))
print(type(y))
print(type(z))
print("\n")

#integer
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

#float
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#complex
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

#type casting
x = float(1)
y = int(2.8)
z = complex(1)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

#convert
x = 5
r = float(x)
print(r)

#random numbers
import random

print(random.randrange(1,10))

