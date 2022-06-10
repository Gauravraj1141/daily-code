with open("gaurav.txt") as f: # ye ek asa function h isme hme file ko close krne ki need nhi h with block ise khud handle krta h
    a1= f.readline() #to isme file pointer ko phli line likhne ke bad dusri line p chora
    a = f.readlines()  # isliye isme agli line se print honi suru hui agr ham seek fun ka use krenge to ye fir suru se lega
    print(a1,"\n",a)



with open("gaurav.txt") as f:
    a1= f.readline()
    f.seek(0) # to hmne yha seek function ka use kiya or pointer ko fir se 0 par le aaye isliye redlines  me suru se sare print hua
    a = f.readlines()
    print(a1,"\n",a)





# f = open("gaurav.txt","rt") # upper jo with block h vo bhi bilkul same work krta h
# print(f.readline())
# print(f.readlines())
# f.close()