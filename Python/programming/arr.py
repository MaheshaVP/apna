myFruits = ['banana','apple','orange']
print(myFruits)

#read
print(myFruits[0])

#update
myFruits[1] = "Ananus"
print(myFruits)

#insert
myFruits.append("mango")
print(myFruits)

myFruits.insert(1,'apple')
print(myFruits)

#remove
myFruits.pop(2)
print(myFruits)

myFruits.pop()
print(myFruits)

#length
print(len(myFruits))

#loop
myFruit = ['apple','beans','cabbage']
for fruit in myFruit:
    print(fruit)

print('\n')

for i in range(len(myFruit)):
    print(myFruit[i])

#finding and break
letters = ['a','b','c','d','e']
print(letters)

for i in range(len(letters)):
    print(letters[i])
    if letters[i] == 'd':
        print('Found')
        break

for i in letters:
    print(i)
    if i == 'c':
        print("found")
        break