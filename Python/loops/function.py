#creation Function
def myFunc():
    print("Hello python")
myFunc()
print('\n')

#arguments passing
def myFunc(fname):
    print(fname + "Reference")
myFunc("Email")
myFunc("Kala")
print('\n')

#two arguments
def myFunc(fname,lname):
    print(fname + "Reference" + lname)
myFunc("Email","verify")
print('\n')

# *args
def myfu(*kid):
    print("The kids are "+kid[1])
myfu("e","mail","verify")
print('\n')

#keyword arguments
def my_function(child3,child2,child1):
    print("The young child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print('\n')

#no of keyword arguments
def myFunction(**name):
    print("last name is " + name["fname"])
myFunction(fname="john",lname="dhube")
print('\n')

#default
def myfunc(country = "ind"):
    print("Im from " + country)
myfunc("jap")
myfunc()
myfunc("Brazil")
print('\n')

#passing list 
def myFunc1(food):
    for x in food:
        print(x)
fruits = ["apple","banana","cherry"]
myFunc1(fruits)
print('\n')

#passing numbers
def func(x):
    return 5 * x
print(func(3))
print(func(4))
print(func(6))
print('\n')

#positional only args
def my_function(x, /):
  print(x)
my_function(3)
print('\n')

#passing  positional and keywords only
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
print('\n')

#recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
print('\n')


#recursion factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(5)
print("factorial is " , result)


def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
factorial = fact(3)
print(factorial)