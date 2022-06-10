"""this is for loop and A for loop is used for iterating (repetetion)
over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements,
 once for each item in a list, tuple, set etc."""
list1 = [["renu",6],["radha",4],["ravi",5],["tanu",9]]
print(len(list1))
print( list1[0],"\n",list1[1] ,"\n",list1[2]) # it is a simple method to print a list.

for m in list1: # we consider m for the all value of list1 in 'm' so we can easily
    # print with the help of for loop,
    # for loop lgane k bad is list me jitne bhi item h vo sabhi print honge
  print(m) # now all value of list 1 store in m so print this and help of for
    # loop sari value ek ke bad ek print hojayegi jab tak us list me value h
for m,n in list1:
    print(m,"ke lollypop is",n)
    # to ase krke ham list ko unpack bhi kr skte h
""" ham list ki jgh dictionary bhi le skte h """
dict1 = dict(list1)
print(dict1) # to ase krke ye sari value dictionary me print ho gyi
# ab is dict me for loop or chalana h
for itmes in dict1:
    print(itmes) # only agr items chiye to ase simple print hojayenge 
for items,lollypop in dict1.items():# hmne yha .itmes() function ka use kiya h
    # yha hmne dict1. itmes() kiya tabhi ye unpack hui h ni to only
    # items hi hore the print lollypop nhi hori thi
    print(items,"ke lollpop is",lollypop)



