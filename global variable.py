f = 10 # ye f global scope me ek  variable h jise sabhi function use kr skte agr unke pas apna koi variable
# nhi h to is nam ka fir vo global scope check krta or vha se us variable ki value leleta h
"""global variable ko kisi bhi program me kitne bhi function use kr skte h agr
uske pas uska private variable nhi h us nam ka to """
def function1(h): # hmneh ek function bnaya jisme ek  h variable liya h
    f = 5 #par ye is function ka personal variable h
    global m # or hmne jse hi m ko global kiya uski value function ke bhr bhi print hogyi kuki ab ye m global hogya
    m = 456
    print(h ,"this is a user define function") #to yah h ki value print kraayi jo ham denge or uske bad jo likha  h vo print hoga
    print(f) # yha ye function ke andr liya h to andr vale f ki value print hogi kuki iske pas iska h agr na hota to
    # ye globally check krta fir global variable ki value print hoti isme
function1("this is the value of h ") # or ye hmne h ki value di h
print(f) # or ye function ke bhr h to isme global vale ki value print hogi
print(m) # hmne yha function ke andr jo m variable h use liya to ye function ke bhr print
#nhi hoskta kuki ye global scope me h ye kabhi bhi function ke andr jake use nhi leskta

k = 9
def function2 (g):
    s= 8
    global k # global keyword ka use krke hi ham global variable ki value change kr skte h
    k = k +2 # hmne ye bhar jo global variable h uski value me 2
    # add kiya par ham asa nhi kr skte kisi functionke andr ye possible nhi bina global keyword ke
    print(k) # to ab ye 11 print krega k ki value
function2("yha ham bat krenge kse global variable ki value ko change kr skte h global keyword se ")


x = 34
def gaurav():
    x = 23
    def rdx():
        global x
        x = 44

    print("before call rdx",x) # yha par x ki value 23 print hui
    rdx()
    print("after call rdx ",x )# or yha par bhi 23 print hui
gaurav()
print(x) #yha x ki value is global keyword ki vjh se 44 print hui agr ye na hota to ye global
# value 34 hi print hoti kuki ye to function ke bhr liya h isliye ye global value lega