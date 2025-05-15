#Array

#Array creation
cars = ["ford","volvo","Ferari"]
print(cars)

#access
cars = ["ford","volvo","Ferari"]
x = cars[1]
print(x)

#modify
cars = ["ford","volvo","Ferari"]
cars[0] = "TATA"
print(cars)

#length
cars = ["ford","volvo","Ferari"]
x = len(cars)
print(x)

#loop
cars = ["ford","volvo","Ferari"]
for x in cars:
    print(x)
    
#append
cars = ["ford","volvo","Ferari"]
cars.append("Honda")
print(cars)

#pop
cars = ["ford","volvo","Ferari","Honda"]
cars.pop(2)
print(cars)

#remove
cars = ["ford","volvo","Ferari","Honda"]
cars.remove("volvo")
print(cars)