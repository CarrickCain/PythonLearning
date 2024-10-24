name = input("What is your name? ")
print("welcome to this adventure", name +".")
def win():
    print("You Win!!")
    

answer = input("You start at a crossroads, would you like to go left or right?(left/right) ").lower()
if answer == 'left':
    answer2 = input("You come to a mountain pass. Would you like to climb it or avoid it?(climb/avoid) ").lower()
    if answer2 == 'climb':
        print("You are attacked by a dragon on the way up. You Died :(")
    elif answer2 =="avoid":
        answer3 = input("A wolf suddenly attacks you. Do you attack or run? (attack/run) ").lower()
        if answer3 == "run":
            print("Think you can out run a wolf?? You Died!!")
        elif answer3 == "attack":
            win()
            quit()
    else:
        print("rocks fall and you die")
elif answer =="right":
    print("you come to a village. Would you like to enter or pass by (enter/pass)")
else:
    print("rocks fall and you die")

print("Thanks for going on this adventure!!")