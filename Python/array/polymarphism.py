class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("move")
        
class boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("sail")

class plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("fly")
        
car1 = car("ford","mustag")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boeing", "747") 
car1.move()
boat1.move()
plane1.move()

#class inheritance
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("move")
        
class car(Vehicle):
    pass

class boat(Vehicle):
    def move(self):
        print("sail")
        
class plane(Vehicle):
    def move(self):
        print("fly")
        
car = car("ford","mustag")
boat = boat("Ibiza", "Touring 20")
plane = plane("Boeing", "747") 

for x in (car,boat,plane):
    print(x.brand)
    print(x.model)
    x.move()
print('\n')
print('\n')

#scope
#locol scope
def Function():
    x = 300
    print(x)
    
Function()
print('\n')

#function inside function
def func():
    x = 100
    def myinnerfunc():
        print(x)
    myinnerfunc()
func()
print('\n')

#global scope
x = 150
def fun():
    print(x)
    
fun()
print(x)
print('\n')

#naming 
x = 150
def fun():
    x=100
    print(x)
    
fun()
print(x)
print('\n')

#global keyword
x = 300
def fun():
    global x
    x = 224
    print(x)
    
fun()
print(x)
print('\n')


