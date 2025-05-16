#f strings
txt = f"The price is 49 dollars"
print(txt)

#placeholders
price = 59
txt = f"The price is {price} dollars"
print(txt)

#operations
txt = f"The price is {20 * 59} dollars"
print(txt)

#functions
fruit = "apple"
txt = f"I love {fruit.upper()}"
print(txt)

#format
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#format
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#named index
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
