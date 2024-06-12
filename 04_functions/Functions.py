# def is known as function 

# question 1

def square(num):
    print(num** 2)

square(4)

#question 2
def add_Two_num(numOne , numTwo):
    return numOne+numTwo

print(add_Two_num(6,98))


#question 3

def multiply(p1,p2):
    return p1 * p2 

print(multiply(6,98)) 
print(multiply(6,"h"))
print(multiply("h",6))


#question 4

def greet(name =  "user"): #  we gave user as default vale , it inplies in second print where no parameter is given
    return "hello" +  name

print(greet("nitin"))
print(greet())

#question 5  =  Lambda function

cube = lambda x : x ** 3

print(cube(3 ))


#question 6 

def sum_all(*args):
   return sum(args)

print(sum_all(1,2,3))
print(sum_all(11,56,98))
print(sum_all(67,87,43))
 
 
 