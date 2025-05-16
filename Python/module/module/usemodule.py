import module

module.greet("Kavya")
print('\n')

a = module.person["country"]
print(a)
print('\n')


#name change
import module as md

a = md.person["age"]
print(a)
print('\n')

#built in module
import platform

x = platform.system()
print(x)
print('\n')

# x = dir(platform)
# print(x)
# print('\n')

from module import person

print(person["name"])