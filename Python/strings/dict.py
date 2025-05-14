#create
thisdict = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964
}
print(thisdict)
print(thisdict["year"])
print(len(thisdict))

thisdict = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
    "colors": ["green", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

#dict
thisdict = dict(name="john",age=20)
print(thisdict)

#access
thisdict = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
    "colors": ["green", "white", "blue"]
}
print(thisdict["model"])
print(thisdict.get("brand"))

#keys
car = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
}
x = car.keys()
print(x)
print('\n')

y= car.values()
print(y)
car["year"] = 1989
print(y)
print('\n')

car["color"] = "green"
print(x)
print(y)
print('\n')

z = car.items()
print(z)
print('\n')

if "color" in car:
    print("s , color is present")

print(car)
print('\n \n')

#change items
car = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
}
car["year"] = 2018
print(car)

car.update({'year':2020})
print(car)
print('\n \n')

#Add items
car = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
}
car["color"] = "yellow"
print(car)

car.update({'engine':'super','color':"red"})
print(car)
print('\n')

#remove
car = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
    'color': "red"
}
print(car)
car.pop("model")
print(car)

car.popitem()
print(car)

car.clear()
print(car)
print('\n')

#loop
car = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
    'color': "red"
}

for x in car:
    print(x)
print('\n')

for x in car:
    print(car[x])
print('\n')

for x in car.keys():
    print(x)
print('\n')

for x in car.values():
    print(x)
print('\n')

for x,y in car.items():
    print(x,y)
print('\n')

#copy
car = {
    "brand":"Ford",
    "model":"mustag",
    "year" : 1964,
    'color': "red"
}
vehicle = car.copy()
print(vehicle)

vehi = dict(car)
print(vehi)
print('\n')

#vehicles
vehicle = {
    "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
}
print(vehicle)
print('\n')