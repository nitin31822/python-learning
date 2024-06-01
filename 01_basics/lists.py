myList  = ["orange" , "green" , "purple"]

## for accessing List Item

print(myList[1])

#answer is green

print(myList[:2])

#answe is first two items

print(myList[2:])

# answer  is from 2 to end


## For changing List Item

myList[1] = "Yellow"
print(myList)

#now the 1 value is changed to "yellow"

myList.insert(1, "Brown")
print(myList)

# now brown is add to 1 item

## for adding  list item 

myList.append("blue")

print(myList)

#now blue add in list

# now for removing item in list 

myList.pop(1)
print(myList)

#answer 1 item remove from list 

# if we did not give any value in pop the the last item item remove from list 