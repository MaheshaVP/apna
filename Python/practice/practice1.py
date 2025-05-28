print("Hello world")

#comment

"""
this is
multiline comment
"""

x =5 
y = "Hello"
print(x)
print(y)

y = int(3)
x = float(3)
print(y)
print(x)

myName = "Mahi"
MyName = "mahi"
my_name = "Mahi"
print(myName,MyName,my_name)

fruits = ["apple","banana","cherry"]
a,b,c = fruits
print(a,b,c)

x = 5
y = "John"
print(x , y)

x = 5
y = 6
print(x+y)

#global
x = "awesome"

def myfun():
    x = 3
    print("word is",x)
    
myfun()

print(x)

#global keyword
x = "good"
def func():
    global x
    x = "fentastic"
func()
print("python is",x)

x = 5
print(type(x))

x = "python"
print(type(x))

x = True
print(type(x))

x = None
print(type(x))

x = 1 
y = 2.0
z = 1j 

print(type(x))
print(type(y))
print(type(z))

y = float(2)
print(y)

#random
import random

print(random.randrange(6,10))

# type casting 
x = int(2.3)
y = float(2)
print(x)
print(y)

print("Hello")
print('Hello')
print("He is called 'Johnny'")

a = "hello"
print(a)
print(a[1])

for x in "cherry":
    print(x)
    
print(len(a))

text = "Hello guru this prema"
print("this" in text)

if "prema" in text:
    print("yes prema is present")
else:
    print("no matching")
    
print("zoho" not in text)

#slicing
b = "hello world"
print(b[6:11])
print(b[:6])
print(b[2:])
print(b[-8:-3])

a = "Hello World  "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('H','J'))

a = "Hello"
b = "world"
c = a + b
d = a+ " "+b
print(c)
print(d)
print(a,b)

price = 48
txt = f"the price is {price}"
print(txt)

txt = f"multiply {2*3}"
print(txt)

x = "hello print"
print(x.capitalize())

print(10>9)
print(10 == 9)
print(10<9)

a = 200
b = 3

if b > a:
    print("b is greater")
else:
    print("a is greater")
    
def fun():
    return True

if fun():
    print("yes")
else:
    print("No")
    
print(10 + 5)

