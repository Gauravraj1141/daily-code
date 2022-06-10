dy1 = {"rahul":{"food":"bhindi "", allu"},"rohan":("kdkdkd","ghgh ","kdkd")}#it is dictionary jse
# hamne rahul ki ek or dictionary bna di ase hi ham iski alg list bhi bna skte h
print(dy1["rohan"])
"""or ye case sensitive hota h isme jis case me dictionary me likha 
hoga usi case me hi likhna hoga jab ham print krangye"""
print(dy1["rahul"]["food"])
dy2 =  {"ram":{"sun":"paobhaji","mon":"tori","tuesday":"loki"},"sohan":{"morning":"rice","evening":"banana"}}
print(dy2["sohan"]["morning"])# so ham yha kitne hi persons ki
# dictionary bna ke unke andr bhi bna ke unhe call kr skte h
"""jse hame is dy2 me kisi or bnde ka data add krne ha to ase krenge """
dy2["gaurav"]= ["chaumin"] # yha hmne dy2 me gaurav ka data bhi add kr dia
dy2[454] = 45451 # to ham yha integer value ka data bhi le skte h or integer value bhi le skte h

del dy2 [454] # agr hame kisi ka data hatana h to del fun ka use krenge
del dy2 ["ram"] # to yha bhi ram ka pura data hi hat gya
print(dy2)
d3 = dy2 # agr ham ab d3  se delte krenge to dy2 se hi hoga kuki vo ise hi represent kr rha h
del d3["sohan"]
print(d3)
dy2.update({"leena":"kdkdk"}) # to ase krke bhi ham add kr skte dictionary me new data ko
print(dy2)
print(dy2.keys())# to ase hamare sari keys print hojayengi jinke bare me hamara data h
print(dy2.items())# to ye hamare key value pairs ko print krta h

