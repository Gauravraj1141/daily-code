# a = 4
# b = 5
# print(v)
 #v = sum((a,b)) # it is a predefine function


def function1(a,b):# ye ek user define function h jo hmne khud banaya h
    print("you are in function1 ",  a+b)
function1(4,6) # to yha hmne value dedi a , b ki jo uper add hogyi
function1(4,45) # ham kitne bhi value le skte h sari upper vale a+b me jake hi exicute hogi

def function2(c,d): #hmne ek or function define kiya jisme ham average nikalenge
    """ye ek doc string jisse hame yad rhta ki ye function average ke liye use kiya to ham
    har function ki doc string ko print kra skte h jisse hame bade code me bhi pta chl jaye ki kis function ka kya kam h """

    average = c+d/2
    print(average)
    return average

    """hmne return ka use isliye kiya jisse v me function ki value store ho jaye or 
    ham v ko print kraya to usme function ki value thi """
print(function2.__doc__) # ye doc string ko print krane k liye use krte h
v = function2(5,6)

print(v) # to ab ye average v me store hogya


