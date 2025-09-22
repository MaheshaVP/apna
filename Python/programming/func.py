#function
def convertToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print(convertToCelsius(80))

#scope
#global

message = "hello world"

def greet():
    print(message)
greet()

#local
def calSum():
    result = 45 + 20
    print(result)

calSum()



