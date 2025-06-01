cars = ["bmw","rr","breeza"]
print(cars)

print(cars[0])
print(len(cars))

for x in cars:
    print(x)
    
    
cars = ["bmw","rr","breeza"]
cars.append("maruthi")
print(cars)

cars.pop(1)
print(cars)


class myClass:
    x = 5
    
p1 = myClass()
print(p1.x)


class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        
p1 = Student("john",32)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
        
p1 = Person("Jeethu",21)

print(p1)


class Person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def myFunc(self):
        print("Hello my name is ", self.name)
        
p = Person1("Jeethu",21)
p.myFunc()


class Per:
    def __init__(one,name):
        one.name = name
        
    def myfun(abc):
        print("my name ",abc.name)
p = Per("Gokul")
print(p.name)
p.name = "kishor"
print(p.name)
print('\n')

# Inheritance
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname + self.lastname)
x = Person("kumar","kalyan")
x.printname()
    

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname + self.lastname)
        
class Student(Person):
    pass

x = Student("Jnana","bharathi")
x.printname()
    
    
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname + self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname, lname)

x = Student("Gokul","krishna")
x.printname()
    
print('\n')

class Manager:
    def __init__(self,name):
        self.name = name
    
    def fun(self):
        print("manager name is",self.name)
        
class emp(Manager):
    def __init__(self, name , year):
        super().__init__(name)
        self.age = year
        
p = emp("Chethan",20)
p.fun()
print(p.age)

print('\n')

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print('\n')

for fruit in mytuple:
    print(fruit)
print('\n')

for letter in mytuple[1]:
    print(letter)
print('\n')

x = mytuple[2]
print(len(x))

# polymorphism
class Car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    
    def Move(self):
        print("drive")
        
class Boat:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    
    def Move(self):
        print("sail")
        
car1 = Car("maruthi","suzuki")
boat1 = Boat("ibriz","rafale")

for x in (car1,boat1):
    print(x.name)
    x.Move()
    print('\n')
    
print("polymorphism")
class Car:
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand
    
    def Move(self):
        print("drive")

class Plane(Car):
    def Move(self):
        print("fly")
        
car = Car("hundai","honda")
plane = Plane("rafale","kota")
for x in (car,plane):
    print(x.name)
    x.Move()
    

x = 300
def myfun():
    def innerfun():
        print(x)
    innerfun()
myfun()
print(x)


def fun():
    x = 100
    print(x)
fun()

def glob():
    global x
    x = 200
    
glob()
print(x)

