# question 1

numbers = [1,-4,6 ,-7,3,7,-6,-9,5]

positive_number_count = 0

for num in numbers:
    if num>0:
        positive_number_count +=1
print("positive numbers  is ",positive_number_count)

#question 2

number = 10
sum_even = 0

for i in range(1,number+1):
  if i%2 == 0:
     sum_even += 1
print("sum of even number is ", sum_even)


#question 3

number = 3

for i in range(1,11):
   if i ==5:
      continue    ##  continue is for removing  5 i 
   print(number,"x",i,"=",number*i)

## question 4  ## resversing str 

input_str = "python"
reversed_str = ""

for char in input_str:
   reversed_str=char+reversed_str ##  reverse_str take one char at time and push to reverse_str which is empty from strat 
print(reversed_str)


#question 5       find first  non repeating char

input_str = "teeter"
for char in input_str:
   if input_str.count(char) == 1:  ## find non repeating char using == 1  
      print("char is ", char)
      break  ## break is used for break loop and end the loop
   
## queston 6     factorial 

number = 5
factorial = 1 

while number>0:
   factorial = factorial*number
   number = number-1

print("factorial value of number is : " ,factorial)

# question 7   getting number in umput from user while he didi not give number in 0 to 10

while True:
  number =  int( input("enter value bw 1 and 10"))
  if 1 <= number <=10:
     print("thanks")
     break
  else:
     print("invalid number , number should be from 1 to 10 : ")


# question 8    check number is prime number 

number = 29 

is_prime  =True

if number> 1:
   for i in range(2,number):
      if (number%i) == 0:
         is_prime= False
         break
print(True)
     






    