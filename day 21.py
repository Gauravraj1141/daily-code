Arithmetic operator

print("5+6 is equal to ",5+6)
print("5*6 is equal to ",5*6)
print("5*6 is equal to ",5*6)
print("5-6 is equal to ",5-6)
print("5**3is equal to ",5**3) # ye 5 ki power 3 kr di ise exponential operator bhi khte h
print("5/6 is equal to ",10/6)# or ye floating point value bhi deta h
print("5//6 is equal to ",10//6) #ye only integer value deta h
print("6%5 is equal to ",6%5) #ye modules operator hota h ye jo remainder bachta
h use dikhata h to 6 ko jab 5 se krenge to remainder 1 bachega


# #Assignment operator
#
x = 5
print(x)
x += 7   # += iski vjh se x me 7 add hogya iska mtlb hoga x= x+7
x *= 7 # ye multiply krega ase hi sare operator kam krenge iske sath me
x /= 7
print(x)
#

# # Comparison operator
#
v = 8
print(v==7) # == ye ek comparison operator h yani ye 7 8 ke barbar nhi h to false show krega
print(v!= 7) # != ye not equal to ka sign h jo bta rha h ki 7 8 ke
# equal nhi h isliye ye true print krega
print(v <= 7) # ye false hoga kuki ye 8 se bda nhi h
print(v >= 7) # ye true hoga kuki ye 8 se chota h

# logical operator
#
a = True
b = False
print(a and b) # kuki and me false ko lega ye agr ek bhi false h dono me se to
print(a and a) # ye to dono true h isliye true hoga
print(a or b ) # or me ye jo bhi ek true hoga use lega
#
# # identity operator

a = True
b = False
print(a is b) # to ye false print krenge kuki ye same nhi h
print(a is not b) # to ye true print hoge kuki ye same nhi vhi ham bhi kh rhe h

# #  Membership operator()

list = [1,5,3,7,44,88,66,99,445]
print(5 in list) # yani 5 list me h to true ayega
print(5 not in list) # yani 5 list me nhi h  to false ayega

# Bitwise operator ()

# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11

print(0|3) # | ye or ka sign h jse 0 = 00 or 3=11 to 01=1,01=1 isliye 11 = 3 print hua
print(0|1) # ase yha 0=00 or 1=01 to 00=0 or 01=1 to 01= 1 hoga
print(0|2) # ase yha 2 aya
print(0&2) # to yha 0 print hoga