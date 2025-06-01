try:
    print(x)
except NameError:
    print(NameError)
except:
    print("exception occured")
    
    
try:
    print("hello world")
except:
    print("some thing error")
else:
    print("nothing error")
    

try:
    print(a)
except:
    print("error")
finally:
    print("finally executed")
    
try:
    f = open("demo.txt")
    try:
        f.write("Hello words")
    except:
        print("error while write")
    finally:
        f.close()
        
except:
    print("smoething went wrong while opening")
    

fruits = "apple"
txt = f"I love {fruits.upper()}"
print(txt)

import math
num = input("enter a number : ")
# calc = math.sqrt(int(num))
# print(calc)

print(f"{int(num)*3}")

name = input("Enter your name : ")
print(f"Hello {name}")

fname = input("enter first name : ")
lname = input("enter last name : ")
print(f"my name is {fname} {lname}")


