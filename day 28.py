f = open("gaurav.txt")
f.seek(0) # ye file pointer ko us no p leaayega jha ham chte h jse hame 20 character ke bad
# se print krna suru krna h to isme 20 likho or vhi se read hogi file
print(f.tell()) # ye f.tell() hame batata h ki hamara file pointer kha par h is time agr
# ham ise readline ke niche lga denge to aagge btayega
print(f.readline()) # to ye function to hamari file ki line by line read krta h
print(f.tell()) # ab ye ek line print hogyi to pointer niche agya to ab 22 no par bta rha h
# to ye file pointer kha stand krra h vo btata h
f.seek(12) # jse hmne yha 12 likha to 12ve character se read krna suru krega ye pointer ko yhi par le aayega
print(f.readline())
print(f.readline())
f.close()