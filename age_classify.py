def age():
    age=int(input("Enter the age:"))
    if 0<=age<=3:
        print("Baby")
    elif 3<age<=12:
        print("Child")
    elif 12<age<=19:
        print("Teen")
    elif 19<age<=40:
        print("Adult")
    elif 40<age<=80:
        print("Old")
    else:
        print("Dead")