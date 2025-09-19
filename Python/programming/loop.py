
#while loop
import random

dice = random.randint(1,6)
print(dice)
count = 1

while dice != 6:
    dice = random.randint(1,6)
    print(dice)
    count += 1
print("you got 6")
print('You rolled', count , 'times')


#for loop
for i in range(10,0,-1):
    print(i)
print('Complete')

#for each
#iteration
myFruits = ['apple','banana','cherry']
for fruit in myFruits:
    print(fruit)

#interation through index
myFruits = ['apple','banana','cherry']
for i in range(len(myFruits)):
    print(myFruits[i])
print('\n')

#do while
count = 0

while True:
    dice = random.randint(1,6)
    print(dice)
    count += 1
    if dice == 6:
        break
print('You got 6')
print('you rolled', count , 'times')

#nested if
numExp = 1000
totalRolls = 0

for i in range(numExp):
    count = 0
    while True:
        dice = random.randint(1,6)
        count += 1
        if dice == 6:
            break
    totalRolls += count

print("Doing",numExp,"experiments")
print('Avg no of rolls to get 6 is', str(totalRolls/numExp))