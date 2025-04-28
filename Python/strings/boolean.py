#check 
print(10 > 9)
print(10 == 9)
print(10 < 9)

#using if 
a = 300
b = 20
if b>a:
    print("b is highest")
else:
    print("a is highest")


print('\n')
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#True
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
print("\n")

#function 
def myfunction():
    return True

print(myfunction())

#funcion using the boolean result
def myfunction():
    return True

if myfunction():
    print("ok")
else:
    print("not ok")