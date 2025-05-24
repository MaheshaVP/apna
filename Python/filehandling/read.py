#open file
f = open("demofile.txt")
print(f.read())
print('\n')

#with open
with open("demofile.txt") as g:
    print(g.read())
print('\n')

#close
f = open("demofile.txt")
print(f.readline())
f.close()
print('\n')

#readline : returns the line
f = open("demofile.txt")
print(f.readline())
print(f.readline())
print('\n')

#looping 
print("For loop")
f = open("demofile.txt")
for x in f:
    print(x)