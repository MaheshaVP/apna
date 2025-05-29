a = 33
b = 200
if b>a:
    print("b is greater than a")


a = 33
b = 200
if a>b:
    print("a is greater")
elif a==b:
    print("equal")
else:
    print("b is greater")
    

a = 33
b = 33
if a>b:
    print("a is greater")
else:
    print("b is greater")

a=8
b=4
if a>b: print("a greater")

a=2
b=200
print("a") if a>b else print("b")


a=2
b=2
print("a") if a>b else print("=") if a==b else print("b") 


a = 200
b = 33
c = 500
if a>b and c>a:
    print("both are geater")
    
if a>b or b>c:
    print("one is corrcet")
    
if not b>a:
    print("b is greater than a")
    
    
day = 5
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
      print("not match")
      
day = 6
match day:
    case 1|2|3|4|5:
        print("week day")
    case 6|7|8:
        print("weekend")
        
month = 6
day = 3
match day:
    case 1|2|3|4|5 if month==5:
        print("week day")
    case 1|2|3|4|5 if month==6:
        print("i love weekend")
        


i = 1
while i < 6:
    print(i)
    i += 1
    
i = 1
while i<=5:
    print(i)
    i+=1
else:
    print("i is no longer than 5")
    
i = 1
while i<=5:
    print(i)
    if i == 3:
        break
    i+=1

i = 0
while i<=5:
    i+=1
    if i == 3:
        continue
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    
for x in "apple":
    print(x)
    

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
    
i = 0
while i < 6:
    i=i+1
    
    if i==4:
        break
    
    print(i)
    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

x = 1
while x<6:
    print(x)
    if x == 3:
        break
    x += 1
    
for x in range(2,6):
    print(x)
    
for i in range(6):
    if i==3: break
    print(i)
else:
    print("finished")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)    
        

print("\n")
def func():
    print("function")
func()

def func(fname):
    print(fname,"function")
func("name")
func("mail")

def func(fname,lname):
    print(fname+" "+lname)
func("kumar","kalyan")
func("john","doy")

def myfunc(*names):
    print("young is",names[1])
myfunc("mail","name","class")

def my_function(**kid):
  print("Her last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def fun(country = "australia"):
    print("country is :",country)
fun("uk")
fun("swidzerland")
fun()


def myfunction(food):
    for x in food:
        print(x)
        
fruits = ["apple","banana","cherry"]
myfunction(fruits)

def fn(x):
    return 5*x

print(fn(3))
print(fn(6))


def recursion(b):
    if(b>0):
        result = b + recursion(b-1)
        print(result)
    else:
        result = 0
    return result
print("recursion result : ")
recursion(4)
print('\n')

def mylam(n):
    return lambda a: a*n
mydoubler = mylam(2)

print(mydoubler(3))

print('\n')
#array
cars = ["ford","volvo","BMW"]
x=cars[0]
print(x)

cars[0] = "toyota"
print(cars)

x = len(cars)
print(x)

for x in cars:
    print(x)
    
cars.append("ferari")
print(cars)

cars.pop()
print(cars)

cars.remove("volvo")
print(cars)

