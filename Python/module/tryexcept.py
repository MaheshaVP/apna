#Try
try:
    print(x)
except:
    print("An exception occured")
print("\n")

#NameError
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("An exception occured")
print("\n")

#else
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print('\n')

#finally
try:
    print("Hello")
except:
    print("Something went wrong")
finally:
    print("The try except finished")
print('\n')

#Raise error
x = -1
if x<0:
    raise Exception("sorry, No numbers below 0")