n = 18
print("you have only 5 attempt to guess the quiz")
v =(0)
while ("v==5"):
    v = v + 1
    num = int(input("enter number that  you  guess =  "))
    print("your attemt =",v,"\n")
    if num > 18 and v<5:
        print("you should input some small number \n ")
    elif num < 18 and v<5:
        print("you should input some big number\n ")
        continue
    elif num == 18:
            print("you won in ",v  ," attempt","\n\n\n")

    else :
        print(" sorry your attempt has been finished \n\t you loss")
        break





