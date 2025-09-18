#dice game
import random

dice = random.randint(1,6)
print("you rolled a dice " + str(dice))

if dice == 6:
    print("You got 6 ! Congrats")
else:
    print("Try again")


#single if 
age  = 34
print("Age is "+ str(age))

if age > 18:
    print("You are an adult")

#else 
age  = 10
print("Age is "+ str(age))

if age > 18:
    print("You are an adult")
else:
    print("you are not an adult yet")


#else if
age  = 15
print("age is " + str(age))

if age < 13:
    print("child")
elif age < 20:
    print("teenager")
else:
    print("Adult")


#nested if

age = 21
print("Age : "+ str(age))

if age < 13:
    print("You are child")
elif age < 20:
    print("teenager")
    if age > 17:
        print("also adult")
else:
    print("You are an adult")

