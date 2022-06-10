n = int(input("enter the number of rows that you want to print \n=\t"))
b = bool(int(input("choose the number between 0 or 1 \n  ")))
"""hmne ye bool function use kiya isme hame true or false ka pta chlta h khud hi 0 hoga to false or 1 hoga to true"""
if b == True:
   print("true")
   i=0
   while i < n:
      print((i + 1) * "*")  # yha hmne i liya kuki i ko n ke brabar krna tha hame or yha pr i+1 isliye kra kuki
   # first time to i ki value 0 rhegi to isliye vo print nhi hoga isliya hmne i ki value suru hi 1 se kri jisse sare print ho
      i = i + 1
elif b == False:
   i = 0
   print("false")
   while i < n:
      print((n) * "*")  # or yha hmne n liya kuki n ko km krke i ke barabar krna tha
      n = n - 1






