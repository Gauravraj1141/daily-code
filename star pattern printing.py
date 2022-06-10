print("welcome to star pattern printing ")
fn = int(input("choose the line of star that you want to print"))
bl = int(input("press 1 for assending order and 0 to desending order "))
g = bl
if g == 1:
    for i in range(0,fn+1): # yha fn+1 to isliye lga dia jisse ye last me 3 print na ho 4 hoja
        print("*"*int(i))
elif g == 0:
        for j in range(fn+1,0,-1):
            print("*"*int(j))
else:
    print("please input the right value ")
