p = 1
while p<=1:
    l = [[(input(" customer name =  ")), int(input(" samose = ")), int(input("burger = ")),int(input(" tikki = ")),int(input("gol gappe in ruppes = "))]]
    for m, s, b ,t,gl  in l:

        print(m, "ne ", s,"samose ", b, "burgur ",t,"tikki",gl," rupees ke golgappe liye ","\nbill of ",m ,"=",(s * 7 + b * 20 + t*15+gl),"rupees \n\n" )  # 1 samosa = 7 rupee,  1burger = 20 rupee , 1 tikki = 15rupe,

    p = int(input("enter 1 for again and 2 for exit = "))

