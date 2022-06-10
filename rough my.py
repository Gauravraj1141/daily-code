def is_leap(year , secondyear):
    for i in range (year,secondyear+1):
        if i%400!=0 and i%4!=0:
            print("     ")
        elif i % 400 == 0 and i% 4 == 0 :
            print("leap")
        else:
            print("leap")
l = int(input("enter year "))
m = int(input("enter second year"))
is_leap(l,m)

