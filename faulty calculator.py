num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))
l = ["+","-","*","/"]
l = input("select you operator")
if num1== 45 and num2== 3 and l == "*":
    print(555)
elif num1 == 56 and num2 == 9 and l == "+":
    print(77)
elif num1 == 56 and num2 == 6 and l == "/":
    print(4)
elif "+" in l:
    print(num1+num2)
elif "-" in l:
   print(num1 - num2)
elif "*" in l:
    print(num1*num2)
elif "/" in l:
    print(num1/num2)
else:
    print("please enter correct input")
