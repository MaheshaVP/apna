#match
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
print('\n')

#default value
day = 4
match day:
    case 2:
        print("Thu")
    case _:
        print("Default")
print('\n')

#combine values
day = 4
match day:
    case 1 | 2 | 3 | 4 :
        print("week days")
    case 5 | 6 :
        print("week end")

#If statements as Guard
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 if month == 4:
        print("week days in april")
    case 1 | 2 | 3 | 4 if month == 5:
        print("week days in may")