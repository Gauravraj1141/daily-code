num1 = input("enter a number")
num2 = input("enter second number")
"""ye hmne isliye use kiya jab ham input ko string de rhe the to error
 aarha tha or usse age ka jo hame line print krani h vo bhi nhi ho rhi 
 thi usse bachne ke liye hmne try or except method ka use kiya isme """
try:
    print("show your result",int(num1)+int(num2))
except Exception as w:
    print(w)
print("this line is very important") # isme ye line bhi print ho gyi try except ki vjh se
