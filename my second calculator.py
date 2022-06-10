var1 = int(input("enter first number"))
var2 = int(input("enter second number"))
l = ["+,-,*,/,%"]
l= (input("please select the operator"))

if "+" in l:
    print(var1+var2)
elif "-" in l:
  print(var1-var2)
elif "*" in l:
 print(var1*var2)
elif "/" in l:
 print(var1/var2)
elif "%" in l:
 print(var1/var2*100)
else :
 print("you are not dial a valid input")


