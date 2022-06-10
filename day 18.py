v = (0)
while(True):# ye True ek saa module h jo kabhi rukta hi nhi h bas chlta hi jata h
    if v<6:
        v=v+1
        continue #to ye jab tak apne se upper ki condition ko false nhi kar
        # deta yani jab tak v ki value 5 tak nhi phuch jati ye jab tak agge nhi badhne dega
        """to yha par v ki value 6 hogyi ab agle line me v
         6 se ginna suru hoga or 45 ke barabar jab tak nhi hojata tab tak break nhi hoga """
    print(v,end="  ") # yha hmne end ka use kiya jisse ye ek hi line me print ho ske yha agr value
    # 1 se start krni h to ham v+1 bhi kr skte h
    v = v+1
    if v == 45 :  # yani jab tak v ki value 45 na ho jaye tab tak ye rukega nhi
        break   # or ise rokne ke liye hmne break statement ka use kiyaa



