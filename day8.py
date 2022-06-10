#today we learn string slicing .
mystr="gaurav is a good boy" # yha hmne ek string leli string me hamesha 0 se counting suruhoti h
print(len(mystr)) #ye is string ki length k liye k iski kitni length h iski length 20 h
print(mystr[5])
"""ye is string ka 5 ka letter print krane ke liye jse iska 5th
letter v h to vo print hoga"""
print(mystr[0:5]) #ase ham 0 se 5 tak ke latter hi print honge
print(mystr[0:20:1])
"""yha ye by default ase hota h skipping ka  1 se suru hota h agr ham yha 
2 lgayenge to 1 skip krke print hoga"""
print(mystr[0:20:2]) # yha ye 1 skip hoke print hoga kuki yha hmne 2 likha h
print(mystr[-1:20]) # yha - ka mean h last se count hoga jse -1 par y ayega
print(mystr[-6:-2]) # yha -6 se -2 tak ke print honge jse od b print hue
print(mystr[0:20:-1]) # ye krke hame puri string ulti likhi hui milegi
mystr="gaurav is a good boy"
print(mystr.isalnum())
"""it is false because in this string no space in words so it is not alphanumeric 
kuki jo alpha numeric hoti h us string me space nhi hota """
mystr2="gauravisagoodboy"
print(mystr2.isalnum())
"""mystr2 me ek bhi space nhi h to yha par isalphanumeric 
true ayega kuki ye alpha h ya yha alpha iske bich me space agr 
nhi hoga to ye alpha hoga """

print(mystr.count("o"))# in this function we can find how often character in
# string jse o yha 3 bar aya
mystr="gaurav is a good boy"
print(mystr.isalnum())
"""it is false because in this string no space in words so it is not alphanumeric 
kuki jo alpha numeric hoti h us string me space nhi hota """
mystr2="gauravisagoodboy"
print(mystr2.isalnum())
"""mystr2 me ek bhi space nhi h to yha par isalphanumeric 
true ayega kuki ye alpha h ya yha alpha iske bich me space agr 
nhi hoga to ye alpha hoga """

mystr="gaurav is a good boy"
print(mystr.count("o")) # when we count how often the character in
# string to count fun ka use krte h
print(mystr.capitalize())# ye string ke first letter ko capital krdeti h
print(mystr.find("good"))# to ye bta rha h 12 ve no p good likha h
# vhi se good likhna start h
print(mystr.upper())# is fun se puri string upper case me hojayegi
print(mystr.lower())# is se puri string lower case me hojayegi
print(mystr.replace("gaurav","sachin"))#to isse gaurav ki jgh sachin ho jayega




