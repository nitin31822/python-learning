# solution 1

age = 25

if age <13:
    print("child")
elif age<20:
    print("Teenager")
elif age <60:
    print("Adult")
else:
    print("Senior")

# Solution 2

age = 22 

day = "thursday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price = price-2

print("ticket price for you is :",price)

#solution 3

score = 86

if score >= 101:
    print("please verify")
    exit()

if score >=90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade B-")
else :
    print("Grade C")

# Solution 4

fruit = "Banana"

color = "Yellow"

if fruit == "Banana":
    if color == "green":
        print("Unripe")
    elif  color == "Yellow":
        print("Ripe")
    elif  color == "Brown":
        print("OverRipe")

# Solution 5

weather = "sunny"

if weather == "Rainy":
     activity = "please stay at home , weather is rainy"
elif weather == "sunny":
    activity = "Go For Walk , Weather is Sunny"
elif weather == "Snow":
    activity = "Snow Wather"

print(activity)


# Solutio 6

order_size = "Medium"

extra_shot = True

if extra_shot:
    coffie = order_size + " Coffie with exta Shot"
else:
    coffie = order_size + " Coffie"

print(coffie)