#tuple creation
thistuple = ("apple", "banana", "cherry","apple", "cherry")
print(thistuple)
print(len(thistuple))

#single item with comma is considered as a tuple
thistuple = ("apple",)
print(type(thistuple))
print('\n')

#tuple datatypes
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1 ,'\n', tuple2 ,'\n', tuple3)
print('\n')


#different datatypes 
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print('\n')

#type
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
print('\n')


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print('\n')

#access tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
print('\n')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:4])
print(thistuple[:4])
print(thistuple[5:])
print(thistuple[-3:-2])
print('\n')

thistuple = ("apple", "banana", "cherry", "orange")
if "orange" in thistuple:
    print("yes orange is in this tuple")
for x in thistuple:
    print(x)
print('\n')

#tuple 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "papaya"
x = tuple(y)
print(x)
print('\n')

#tuple convert to list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("grape")
thistuple = tuple(y)
print(thistuple)
print('\n')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
print('\n')

#remove item from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove(y[1])
thistuple = tuple(y)
print(thistuple)
print('\n')

#unpacking a tuple
fruits = ("apple","banana","cherry")
(a,b,c) = fruits
print(a)
print(b)
print(c)
print('\n')


fruits = ("apple","banana","cherry","strawberry", "raspberry")
(a,b,*c) = fruits
print(a)
print(b)
print(c)
print('\n')

#loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
print('\n')

thistuple = ("apple", "banana", "cherry")
for x in range(len(thistuple)):
    print(thistuple[x])
print('\n')

thistuple = ("apple", "banana", "cherry")
i = 0
while i<len(thistuple):
    print(thistuple[i])
    i = i + 1

#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)