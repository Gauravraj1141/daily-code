"""isme ham only 1 digit ko ek hi bar print kra skte h or agr kisi
bhi digit ka repetetion hoga to vo print nhi hogi yhi khas bat hoti h
 set m ise समु्च्चय bhi khte h  jo ek tarah ki anek chijo ka smuh """
s = set({1,2,3,4,5}) # ham koi bhi ek empty set le skte h
print(type(s)) # isse iska type pta chalega yani ye ek set h
s.add(1) # hmne yha 1 add kraya to 1 hamre set m phle se hi tha to isliye 1 do bar print nhi hoga
s.add(9) # or ye 9 diff h to isliye ye us set m add hogya
# only 1 hi bar print hoga isme koi bhi value repeat nhi hoti
s.add("kdkd") # isme har string bhi add kr skte h
print(s)
#s1 = s.union({8,9,7}) # ye ek nya set bna deta h
s1 = s.intersection({1,4}) # yha ye s or s1 me jo common h use print krega
s1 = s.isdisjoint(s)
s.remove(2) # isse hmne s me se 2 ko remove kraya h
print(s,s1)  # yha hmne dono ko karaya






