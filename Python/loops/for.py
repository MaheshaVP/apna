#for loop
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
print('\n')

#for one word
for x in "apple":
    print(x)
print('\n')

#break
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
print('\n')

#loop check at first
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
print('\n')

#continue
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
print('\n')

#range
for x in range(5):
    print(x)    
print('\n')


for x in range(2,5):
    print(x)    
print('\n')


for x in range(2,35,5):
    print(x)    
print('\n')

#else in for loop
for x in range(1,5):
    print(x)    
else:
    print("finally finished")
print('\n')

#nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x,y)
print('\n')