#Arithmetic operators
x = 8
y = 6

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)
print('\n')


#assignment
x = 5
x += 5

print(x)
print('\n')

#comparision 
x = 5
y = 6
print(x==y)
print(x!=y)
print('\n')

#logical 
x = 5
print(x>4 and x<10)
print(x < 10 or x > 5)
print(not(x>4 and x<4))
print('\n')

#identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(z is x)
print(x is y)
print(x==y)

print( x is not z)
print( x is not y)
print(x != y)
print('\n')

#membership operator
y = ["apple", "banana"]
print("apple" in y)
print("pine" not in y)
print('\n')

#bitwise operator
print(5&3)
print(6|5)