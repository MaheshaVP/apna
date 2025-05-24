#delete
# import os
# os.remove("file2.txt")

#check file
import os
x = "file3.txt"
if os.path.exists(x):
    os.remove(x)
    print("file deleted")
else:
    print("the file doesn't exist")

