# sets did not allowed duplicate values

myList  = {"orange" , "green" , "purple","orange"}
print(myList)

#anser is last orange is removed from sets because sets did not allowd duplicate valus

# true and 1  is consederd as same in sets
# false and 0 is considered as same in sets

# for knowing the length 

print(len(myList))


## for checking the item from sets

print( "orange" in myList) # the answer is true

## for adding the item in sets

myList.add("blue")
print(myList)

## for removing the item  in set just use remove like

myList.remove("green")
print(myList)