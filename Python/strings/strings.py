#strings
print("Hello")
print('Hello \n')

#quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"\n')

#assign strings to variables
x = "hello"
y = 'hello'
print(x)
print(y,"\n")

#multiline strings
a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""

a = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

print(a)

#strings are array
a = "Hello , world"
print(a[1])

#loops through a string
for x in "apple":
    print(x)
print("\n")

#length of stri
a = "Hello , world"
print(len(a))
print("\n")

#check string
txt = "The best things in life are free!"
print("free" in txt ,'\n')

#using if 
txt = "The best things in life are free!"
if 'freed' in txt :
    print("yes , 'free' is present \n")


#check if not
txt = "The best things in life are free!"
print("free" not in txt ,'\n')

#using if 
txt = "The best things in life are free!"
if "expense" not in txt:
    print("yes , 'expense' is not present \n")


#slicing string
a = "Kathana"
print(len(a))
print(a[2:8] , '\n')
print(a[:4])
print(a[2:])
print(a[-4:-1],"\n")

#name capitalize
name = "mahesh"
x = name[0:1].upper()
print(x+name[1:],'\n')

#uppercase
a = "Hello, World!"
print(a.upper(), '\n')

print(a.lower(), '\n')

print(a.strip(),'\n')    #white  space

print(a.replace("H","Q"))

print(a.split(","))

#concatenate strings
a = "Hello"
b = "World"
c = a + b
print(c)

#add space
a = "Hello"
b = "World"
c = a + " " + b
print(c)

a = "join"
b = "the"
c = "party"
print(a+b+c,'\n')

#format strings
age = 36
txt = "My name is John, I am ", age
print(txt)
print('\n')

#f-strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 42
txt = f"The price is {price} pounds"
print(txt)

price = 42
txt = f"The price is {price:.2f} pounds"
print(txt)

t = f"The price is {2 * 26} pounds"
print(t)

#escape character
quote = "\n we are called the \"vikings\" from the north"
print(quote)
print("\n")

