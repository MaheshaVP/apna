#write file append
a = open("demofile1.txt","a")
a.write(" now it has written one more line")

a = open("demofile1.txt")
print(a.read())
print('\n')

#write overwrite
b = open("demofile.txt")
print(b.read())

print("----------------------------------")
b = open("demofile.txt","w")
b.write("Movies are waste of time then waste the time on books")

b = open("demofile.txt")
print(b.read())

#new file
c = open("file2.txt","x")

c = open("file2.txt","w")
c.write("Hello guru")

c = open("file2.txt")
print(c.read())

