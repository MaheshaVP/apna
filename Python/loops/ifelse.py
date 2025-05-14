#if
a = 33
b = 200
if b > a:
    print("b is greater")
print('\n')

#elif
a = 10
b = 10
if a > b:
    print("a is greater")
elif a==b:
    print("a is equal to b")
print('\n')

#else
a = 200
b = 33
if b > a:
    print("b is greater")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater")
print('\n')

#without elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print('\n')

#short hand if
a = 200
b = 33
if a>b: print("a is greater")
print('\n')

#short hand if else
a = 2
b = 16
print("A") if a>b else print("B")
print('\n')

#three conditions
a = 300
b = 300
print("A") if a>b else print("equal") if a==b else print("B")
print('\n')

#and
a = 200
b = 33
c = 500
if a>b and c>a:
    print("both conditions are equal")
print('\n')

#or
a = 200
b = 33
c = 500
if a>b or a>c:
    print("atleast one conditions are true")
print('\n')

#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
print('\n')

#nested
x = 20

if x>10:
    print("print above 10")
    print("\n")
    if x > 15:
        print("print also above 15")
        print("\n")
    else:
        print("not 20")

#pass
a = 33
b = 200

if b > a:
  pass