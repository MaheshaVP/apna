import re

txt = "The rain in spain"
x = re.findall("ai",txt)
print(x)
print('\n')

txt = "The rain in spain"
x = re.split("\s",txt)
print(x)

#pip
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))