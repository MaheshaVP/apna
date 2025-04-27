#global variable
x = "awesome"

def myFunc():
    print("python is " , x , "\n")

myFunc()


#using in global and local
x = "awesome"

def myFunc():
    x = "known as super"
    print("python is " + x )

myFunc()

print("python is " + x + "\n")

#use the local variable as global variable
def glob():
    global e
    e = "good"
glob()

print("This is " + e)

#change the global var in local
e = "spicy"
def glob():
    global e
    e = "mindblowing"
glob()

print("This is " + e)

