thislist = ["apple","banana","cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

# tlist = list(("apple","banana","cherry"))
# print(type(tlist))

print(thislist[1])
print(thislist[-1])
if "cherry" in thislist:
    print("yes cherry is present")
    
thislist[1] = "current"
print(thislist) 


thislist.insert(1,"banana")
print(thislist)

thislist.append("piku")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop(2)
print(thislist)

thislist.append("gazzri")
print(thislist)

for x in thislist:
    print(x)
    
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
    
thislist = ["apple", "banana", "cherry"]
newlist = []

for x in thislist:
    if "a" in x:
        newlist.append(x)
        
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1 = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
thislist1.sort()
print(thislist1)

mylist = thislist.copy()
print(mylist)

myli = list(thislist)
print(myli)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


for x in list2:
    list1.append(x)
    
print(list1)

list1.extend(list2)
print(list1)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

y = list(thistuple)
y[1]  = "cuury"
y.remove("apple")
x = tuple(y)
print(x)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
    
for i in range(len(thistuple)):
    print(thistuple[i])
print('\n')
    
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
print('\n')


thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
    print(x)

set1 = {1,2,3}
set2 = {'a','b','c'}
set3 = set1.union(set2)
print(set3)

thisdict = {
    "brand":"ford",
    "model":"mustag",
    "year":1986
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

thisdict["year"] = 1996
print(thisdict)

thisdict["color"] = "green"
print(thisdict)

thisdict.pop("model")
print(thisdict)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

mydict = thisdict.copy()
print(mydict)



