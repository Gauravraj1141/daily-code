# f = open("gaurav diet.txt","w") # ye hmne file open kri ek new file bn gyi isi se
# # # hmne "w" liya h yani write krne ke liye ham file me jo bhi likhenge vo add hojayega usme
# # f.write("gaurav ek very cute boy h \n\t")
# f.close() # file ko kholte h to band bhi krni jaruri h
#
# f = open("gaurav diet.txt","a") # ye "a" append function isse ham file ke last me har
# # bar run krane par jod skte h vo har bar add hota chala jata h
# f.write("gaurav is a good boy") # jitni bar bhi run krayenge utni bar ye file me
# # add hota chala jayega
# a= f.write("gaurav is a good boy") # ise variable a me dal ke hm check kr
# # skte h character number kitne h
# print(a) # or a ko print kra dia

# handle read & write

f= open("gaurav diet.txt", "r+") # ye "r+" isliye liya jab ham file ko read bhi
# krna chte h or write bhi krna chte h
print(f.read()) # to vo print ho jayga jo is file me hoga phlese hi ab hme write bhi krna h
f.write("this boy is very cute") # to ye bhi file me add hogya h