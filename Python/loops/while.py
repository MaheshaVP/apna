#while
i = 1
while i<6:
    print(i)
    i += 1
print('\n')

#break
i = 1
while i<6:
    print(i)
    if i == 4:
        break
    i += 1
print('\n')

#continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
print('\n')

#if else
i = 1
while i<6:
    print(i)
    i += 1
else:
    print("i is no longer than 6")