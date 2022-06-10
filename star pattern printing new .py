c = 1
while c <=1:
    p = int(input("press 1 for increaseing patter printing and press 2 for decreasing pattern printing \n = "))
    if p == 1:
        l = int(input("enter number that you want to print line of star pattern \n ="))
        v = 1
        while v <= l:
            print("*" * v)
            v += 1
    elif p == 2:
        l = int(input("enter number that you want to print line of star pattern \n ="))
        v = 1
        while v <= l:
            print("*" * l)
            l = l - 1
    else:
        print("sorry please enter a valid input \n = ")
    c = int(input("press 1 for again and press 2 for exit = "))
    print("\n\n\tthanku")






