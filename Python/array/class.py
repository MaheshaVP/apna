#class creation
class myClass:
    x = 5
    
p1 = myClass()
print(p1.x)
print('\n')

#init function
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("john",24)
print(p1.name)
print(p1.age,'\n')

#str method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
    
p1 = Person("john",24)
print(p1)
print('\n')

#object methods
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        
    def myfunc(self):
        print("my name is " + self.name)

p1 = Person("kishor",24)
p1.myfunc()
print('\n')

#any name in the place of self
class Student:
    def __init__(silly,name,std):
        silly.name = name
        silly.std = std
    
    def func(abcd):
        print("my std is " + abcd.std)
        
p1 = Student("kavya","xii")
p1.func()
print('\n')

#modify
class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        
    def myfunc(self):
        print("my name is " + self.name)
        print("my age is " , self.age)


p1 = Person("kishor",24)
p1.myfunc()
print("\n")

p1.age = 56
print("afetr modify" , p1.age)
print('\n')

# del p1
# print(p1)

