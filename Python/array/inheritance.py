#Inheritance

#parent class
class Person:
    def __init__(self,fname,lname):  #properties
        self.fname = fname
        self.lname = lname
        
    def printName(self):  #method
        print("full name is",self.fname,self.lname)
        
class Student(Person):          #child class
    pass

x = Student("abhishek","ram")
x.printName()
print('\n')


#init function
class Person:
    def __init__(self,fname,lname): 
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print("full name is",self.fname,self.lname)
        
class Student(Person):          
    def __init__(self, fname, lname):
        Person.__init__(self,fname, lname)

x = Student("kiran","kumar")
x.printName()
print('\n')


#super function
class Person:
    def __init__(self,fname,lname): 
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print("full name is",self.fname,self.lname)
        
class Student(Person):          
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("bharath","koutilya")
x.printName()
print('\n')


#add parameter
class Person:
    def __init__(self,fname,lname): 
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print("full name is",self.fname,self.lname)
        
class Student(Person):          
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.passedyear = year

x = Student("nitin","king",2024)
x.printName()
print(x.passedyear)
print('\n')


#add methods
class Person:
    def __init__(self,fname,lname): 
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print("full name is",self.fname,self.lname)
        
class Student(Person):          
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.passedyear = year
    
    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.passedyear)

x = Student("nitin","king",2024)
x.welcome()
print('\n')


#Inheritance
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print(self.fname,self.lname)
        
# x = Person("virat","kohli")
# x.printName()

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduate = 2024
        
    def welcome(self):
        print(self.fname,self.lname,"The graduation year is ",self.graduate)
    
n = Student("ishan","kishan")
n.welcome()

