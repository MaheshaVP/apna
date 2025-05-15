#Iterator list
mytuple = ("apple", "banana", "cherry","dragon")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#string
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#loop
mytuple = ("apple", "banana", "cherry","dragon")
for x in mytuple:
    print(x)
    
mystr = "apple"
for x in mystr:
    print(x)
    
#using class
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter))


