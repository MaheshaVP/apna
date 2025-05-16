#input
# print("Enter your name")
# name = input()
# print(f"Hello {name}")

#prompt
# name = input("Enter name : ")
# print(f"I Love {name}")
# print('\n')

#multiline inputs
# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

#math
# import math
# x = input("Enter a number : ")
# y = math.sqrt(float(x))
# print(f"The square root of {x} is {y}")

#validate
y = True
while y == True:
    x = input("number")
    try:
        x = float(x)
        y = False
    except:
        print("wrong input please  try again")
print('thank you')
