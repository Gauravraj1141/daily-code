def get_date_time():
    import datetime
    return datetime.datetime.now()

print("welcome to health management system ")



def log():

    print("choose the person that you want to lock his activity so choose \n 1. for Gaurav \n 2. for Rdx\n 3. for Aatif")
    inp = int(input())

    if inp == 1:
        t = 1
        while t <=1:
            print("choose the activity that you want to lock  \n 1.for Diet \n 2.for Excercise = ")
            activity = int(input())
            if activity == 1:
                with open("gaurav diet.txt","a") as d:
                    data = input("= ")
                    d.write("="+str(str(get_date_time())) +"\t " +data+ "\n"  )
                    t = int(input("if you want to login again \n 1.for yes \n 2. for no "))
            else:
                with open("gaurav excercise.txt","a") as d:
                    data = input("= ")
                    d.write( str(str(get_date_time())) +"\t " +data+ "\n"  )
                t = int(input("if you want to login again \n 1.for yes \n 2. for no "))
    elif inp == 2:
        t1 = 1
        while t1 <=1 :
            print("choose the activity that you want to lock  \n 1.for Diet \n 2.for Excercise")
            activity = int(input())
            if activity == 1:
                with open("rdx diet.txt", "a") as d:
                    data = input("= ")
                    d.write(str(str(get_date_time())) +"\t"+ data + "\n")
                    t1 = int(input("if you want to login again \n 1.for yes \n 2. for no "))
            else:
                with open("rdx excercise.txt", "a") as d:
                    data = input("= ")
                    d.write(str(str(get_date_time()))+"\t" + data + "\n")
                t1 = int(input("if you want to login again \n 1.for yes \n 2. for no "))
    elif inp == 3:
        t2 = 1
        while t2 <= 1:
            print("choose the activity that you want to lock  \n 1.for Diet \n 2.for Excercise")
            activity = int(input())
            if activity == 1:
                with open("attif diet . txt", "a") as d:
                    data = input("= ")
                    d.write(str(str(get_date_time())) +"\t" + data + "\n")
                    t2 = int(input("What do you want to login again \n 1.for yes \n 2. for no "))
            else:
                with open("attif  excercise .txt", "a") as d:
                    data = input("= ")
                    d.write(str(str(get_date_time()))+"\t" + data + "\n")
                t2 = int(input("What do you want to login again \n 1.for yes \n 2. for no "))

    else :
        print("please choose right option to lock you activity")

def retrive():
    print("choose the person that you want to retrive his activity \n 1. for Gaurav \n 2. for Rdx\n 3. for Aatif")
    inp = int(input())
    if inp == 1:
        t4 = 1
        while t4 <=1 :
            print("choose the activity that you want to retrive  \n 1.for Diet \n 2.for Excercise")
            activity = int(input())
            if activity == 1:
                with open("gaurav diet.txt", "r") as r:
                    c = r.read()
                    print(c)
                    t4 = int(input("What do you want to retrive this data agian , so press  \n 1. for yes \n 2. for no  "))
            else:
                with open("gaurav excercise.txt","r") as d:
                    c = d.read()
                    print(c)

                    t4 = int(input("What do you want to retrive this data agian , so press  \n 1. for yes \n 2. for no "))

    elif inp ==2:
        t5 = 1
        while t5 <= 1 :
            print("choose the activity that you want to retrive  \n 1.for Diet \n 2.for Excercise")
            activity = int(input())
            if activity == 1:
                with open("rdx diet.txt", "r") as r:
                    c = r.read()
                    print(c)
                    t5 = int(input("What do you want to retrive this data agian , so press  \n 1. for yes \n 2. for no  "))
            else:
                with open("rdx excercise.txt", "r") as d:
                    c = d.read()
                    print(c)
                    t5 = int(
                        input("What do you want to retrive this data agian , so press  \n 1. for yes \n 2. for no "))

    elif inp == 3:
        tern = 1
        while tern <=1 :
            print("choose the activity that you want to retrive  \n 1.for Diet \n 2.for Excercise")
            activity = int(input())
            if activity == 1:
                with open("attif diet . txt", "r") as r:
                    c = r.read()
                    print(c)
                    tern = int(input("What do you want to retrive this data agian , so press  \n 1. for yes \n 2. for no  "))
            else:
                with open("attif  excercise .txt", "r") as d:
                    c = d.read()
                    print(c)
                    tern = int(input("What do you want to retrive this data agian , so press  \n 1. for yes \n 2. for no "))

    else:
        print("enter a valid input")

print("please choose  what do you want = \n 1 for log\n "
      "2 for retrive")
inp = int(input())
if inp == 1:
    print(log())
else:
    print(retrive())






