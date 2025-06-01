import module 

module.greet("Mahesh")

a = module.person1["age"]
print(a)

import module  as md
print(md.person1["qualify"])


import platform
x = platform.system()
print(x)


from module import list

x = list[1]
print(x)
print('\n')

import datetime
t = datetime.datetime.now()
print(t)

print(t.year)
print(t.strftime("%A"))
print(t.strftime("%B"))


x = min(2,3,4)
y = max(2,3,4)
print(x)
print(y)


x = pow(4,3)
print(x)

import math

x = math.sqrt(64)
print(int(x))

x = math.pi
print(x)


import json
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["city"])


person1 = {
    "name" : "mahesh",
    "age" : 21,
    "qualify" : "BCA"
}

a = json.dumps(person1)
print(a)

import camelcase

c = camelcase.CamelCase()
txt = "lorem ipsum dolor sit amet"
print(c.hump(txt))


