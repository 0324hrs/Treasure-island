##### conditional statements ...if else statements########
print("Yoh, welcome to the rollacoaster ride")

# 
height= int(input("what is your height in cm? \n"))
age = int(input("what is your age?\n"))
# conditional statement....nested
if height >= 120:
    if age >= 18:
        print("You will have to pay ksh 2500 to go for the rollacoaster ride")
    else:
        print("You will have to pay ksh 2000 to go for the rollacoaster ride")
else:
    print("You cannot go for the rollacoaster ride")
        
    
    
########odd or even exercise:modulo operator##########
print("hello there, welcome to the odd or even number checker")

int_input = int(input("what is the number you want to check  \n"))

# 
if int_input % 2 == 0:
    print("the  is even")
else:
    print("the number number is odd")
###########################
    
#####elif comdition#####
print("Yoh, welcome to the rollacoaster ride")

# 
height= int(input("what is your height in cm? \n"))
age = int(input("what is your age?\n"))
# conditional statement....nested
if height >= 120:
    if age <= 10:
        print("you will pay ksh 400 for the rollacoaster ride")
    elif age<=14:
        print("you will have to pay ksh 650 for the rollacoaster ride")
    elif age <=17:
        print("you will pay ksh 1000for the rollacoaster ride")
    elif age >=18:
        print("you will have to pay ksh 1600 for the rollacoaster ride")
else:
    print("you cannot go for the rollacoaster ride")


###########exercise..leap year challenge###########
# 
year = int(input("which year do you want to check?\n"))
# 

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("not a leap year")
        
else:
    print("not a leap year")
    
#######################################
####pizza order system exercise###########

print("welcome to pizza orders delivery")
# 
size = input("what size do you want? S, M or L\n")
add_pepperoni = input("do want pepperoni added? Y or N\n")
add_extra_cheese = input("do you want extra cheese added? Y or N\n")
# 

bill = 0
# cmprson
if size == "S":
    bill += 20 
elif size == "M":
    bill += 50
elif size == "L":
    bill += 100
# 
if add_pepperoni == "Y":
    if size == "S":
        bill += 10
    else:
        bill += 20
# 
if add_extra_cheese == "Y":
    bill += 15
else:
    bill
    
print(bill)

##########logical operator#######
#####and-both conditions are true
######or-one of the conditions is true
#####love calculator,huh#####
print("Hello there,welcome to the love calculator")
# 
name1 = input("what is your name?\n")
name2 = input("what is his/her name?\n")
# lower() and count() functions used
combined_names = name2 + name1
# convert everything to lowercase
lower_case_names = combined_names.lower()
#check out the letters true
t = lower_case_names.count("t") 
r = lower_case_names.count("r") 
u = lower_case_names.count("u") 
e = lower_case_names.count("e") 
# 
true = t + r + u + e

# check out the letters count for love
l = lower_case_names.count("l")
o = lower_case_names.count("o")
v = lower_case_names.count("v")
e = lower_case_names.count("e")
# 
love = l + o + v + e
# 
loveScore = (love) + (true)

# 
if (loveScore < 10) or (loveScore > 90):
    print(f"your love score is {loveScore} joh")
elif (loveScore >= 40) and (loveScore <= 50):
    print(f"your love score is {loveScore} and you're frauds")
else:
    print("You're another fraud")
# print(loveScore)