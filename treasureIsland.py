print("Welcome to the treasure island,your mission is to find the treasure")
# 

direction = input("which direction do you want to go? left or right \n")
# 
if direction == "left":
    boat_or_swim = input("you have have come to a beach,do you want to swim or wait for a boat? \n")
    if boat_or_swim == "wait":
        door_choices = input("which door do you wanna open? red, yellow or green \n")
        if door_choices == "green":
            print("Hurrah, you've found the treasure folk")
        else:
            print("Boom!, you've died due to bomb expulsions")
    else:
        print("You've been eaten by a shark, RIP folk")
    
     
else:
    print("game over folk")
    