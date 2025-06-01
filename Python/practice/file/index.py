print("File handling")

f = open("demo.txt")
print(f.read())

with open("demo.txt") as f:
    print(f.readline())
    print(f.readline())


with open("demo.txt") as f:
    for x in f:
        print(x)
        
print('\n\n')

# write
with open("demo.txt","a") as f:
    f.write("adding a content")
    
with open("demo.txt") as f:
    print(f.read())
    
f = open("demo1.txt","w")
f.write("tfi is the best movie content")

f = open("demo1.txt")
print(f.read())

#create
f = open("demo2.txt","x")
f.write("NU is my Highest Education")

f = open("demo2.txt")
print(f.read())


import os 
if os.path.exists("demo3.txt"):
    os.remove("demo3.txt")
else:
    print("file does not exists")
