def get_date_time():
    import datetime
    return datetime.datetime.now()

inp = int(input("choose the number that you want \n  press  1. for gaurav \n  press  2. for rdx\n  press  3. for attif\n  = "))
if inp in [1, 2, 3]:
    print("welcome to our health management system ")
else :
    print("please enter a valid numer")
if inp == 1:
    while(True):
        print("Enter 'D' for diet \nEnter 'E' for excercise\nEnter 'y' for exit ")
        l = input("it is for gaurav\n  =")

        if l == "D":
            with open("gaurav diet.txt") as d:
                content = d.read()
                print(content,"\n\n")
        elif l== "E":
            with open("gaurav excercise.txt") as e:
                content = e.read()
                print(content,"\n\n" )
                continue
        else:
            print("Thank you")
            break
elif inp == 2:
    while (True):
        print("Enter 'D' for diet \nEnter 'E' for excercise\nEnter 'y' for exit ")
        l = input("it is for rdx \n  =")
        if l == "D":
            with open("rdx diet.txt") as d:
                content = d.read()
                print(content,"\n\n")
        elif l == "E":
            with open("rdx excercise.txt") as e:
                content = e.read()
                print(content,"\n\n")
                continue
        else:
            print("Thank you ")
            break
elif inp == 3:
    while (True):
        print("Enter 'D' for diet \nEnter 'E' for excercise\nEnter 'y' for exit ")
        l = input("it is for aatif \n  = ")
        if l == "D":
            with open("attif diet . txt") as d:
                content = d.read()
                print(content,"\n\n")
        elif l == "E":
            with open("attif  excercise .txt") as e:
                content = e.read()
                print(content,"\n\n")
                continue
        else:
            print("Thanku You")
            break










