#Create list
myList = ["apple","banana","cherry"]
print(myList)

#duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist , '\n')

#length
myList = ["apple","banana","cherry","dogger"]
print(len(myList) , '\n')

#list any datatypes
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3 , '\n')

#a list contain different datatypes
list1 = ["abc", 34, True, 40, "male"]
print(list1,'\n')

#type
mylist = ["apple", "banana", "cherry"]
print(type(mylist) , '\n')

#list constructor
mylist = list(("a","b","c"))
print(mylist)

#list indexing
mylist = ["a","b","c","d","e"]
print(mylist[1])
print(mylist[-1])
print(mylist[2:5])
print(mylist[1:])
print(mylist[:4])
print(mylist[-5:-2])

#check using in
print('\n')
mylist = ["a","b","c","d"]
if "a" in mylist:
    print("yes, 'a' is present in the list \n")

#change list items
myList = ["a","b","c","d"]
myList[1] = "f"
print(myList)

#change range of items
mylist = ["a","b","c","d"]
mylist[1:3] = ["f","g"]
print(mylist)
print('\n')

mylist = ["a","b","c","d"]
mylist[1:2] = ["f","g"]
print(mylist, '\n')

mylist = ["a","b","c","d"]
mylist[1:4] = ["q"]
print(mylist,'\n')

#insert items
mylist = ["apple","banana","cherry"]
mylist.insert(2,"watermilon")
print(mylist)

mylist = ["a","b","c","d"]
mylist.insert(2,"d")
print(mylist, '\n')

#Add list items
#append
mylist = ["a","b","c"]
mylist.append("d")
print(mylist,'\n')

#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
print('\n')

#extend add two list values
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
print('\n')

#add any list or tuple
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange") #tuple
thislist.extend(thistuple)
print(thislist,'\n') 

#remove
mylist = ["a","b","c"]
mylist.remove("b")
print(mylist,'\n')

#pop specified index using 
mylist = ["a","b","c","d"]
mylist.pop(3)
print(mylist,'\n')


mylist = ["a","b","c"]
del mylist[1]
print(mylist,'\n')

mylist = ["a","b","c","d"]
mylist.pop()
print(mylist,'\n')

#clear
mylist = ["a","b","c","d"]
mylist.clear()
print(mylist,'\n')

#list using loop
mylist = ["a","b","c","d"]
for x in mylist:
    print(x)
print("\n")

#range
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print('\n')

#while loop
mylist = ["a","b","c","d"]
i = 0
while(i<len(mylist)):
   print(i,'=',mylist[i])
   i=i+1
print('\n')

mylist = ["a","b","c","d"]
[print(x) for x in mylist]
print('\n')

#list comprahension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
   if "a" in x:
    newlist.append(x)
print(newlist)
print('\n')

#newlist
mylist = ["a","b","c","d","g"]
newlist = [x for x in mylist]
print(newlist)
print('\n')

#range
newlist = [x for x in range(9) if x<5]
print(newlist)
print('\n')

#upper
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
print('\n')

#sorted list alphabatically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print('\n')

#numbers list
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print('\n')

#reverse
mylist = ["a","b","c","d","g"]
mylist.sort(reverse=True)
print(mylist)
print('\n')

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
print('\n')

#case sensitive
thislist = ["orange", "MAngo", "Kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print('\n')

#reverse
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.reverse()
print(thislist)
print('\n')

thislist = ["orange", "MAngo", "Kiwi", "pineapple", "banana"]
thislist.sort(key = str.lower)
print(thislist)

#copy
print('\n')
thislist = ["orange", "Kiwi", "pineapple", "banana"]
mylist = thislist.copy()
print(mylist)

#list
print('\n')
thislist = ["orange", "Kiwi", "pineapple", "banana"]
mylist = list(thislist)
print(mylist)

#using slice
print('\n')
thislist = ["orange", "Kiwi", "pineapple", "banana"]
mylist = thislist[:]
print(mylist)

#join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#append
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
   list1.append(x)
print(list1)

#extend
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)