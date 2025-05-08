#sets creation
thisset = {"apple","banana","cherry","dragon"}
print(thisset)
print(len(thisset))
print(type(thisset))

#set constructor
thisset = set(("banana","cherry","dragon"))
print(thisset)
print('\n')

#access
thisset = {"apple","banana","cherry","dragon"}
for x in thisset:
    print(x)
print('\n')


if "banana" in thisset:
    print("yes")
print('\n')


#add items
thisset = {"apple","banana","cherry","dragon"}
thisset.add("papaya")
print(thisset)
print('\n')

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
print('\n')

#remove
thisset = {"apple","banana","cherry","dragon"}
thisset.remove("banana")
print(thisset)
print('\n')

thisset = {"apple","banana","cherry","dragon"}
thisset.discard("banana")
print(thisset)
print('\n')

thisset = {"apple","banana","cherry","dragon"}
x = thisset.pop()
print(x)
print(thisset)
print('\n')


thisset.clear()
print(thisset)
print('\n')

#loop
thisset = {"apple","banana","cherry","dragon"}
for x in thisset:
    print(x)
print('\n')

#join sets
x = {"a","b","c"}
y = {1,2,3}
z = x.union(y)
print(z)
print('\n')

x = {"a","b","c"}
y = {1,2,3}
x.update(y)
print(x)
print('\n')


#difference
x = {"a","b","c",1,2}
y = {1,2,3}
z = x.intersection(y)
print(z)
print('\n')

x = {"a","b","c",1,2}
y = {1,2,3}
z = x.difference(y)
print(z)
print('\n')