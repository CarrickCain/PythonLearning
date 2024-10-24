import random

ceiling_of_range = input("enter a number: ")

if ceiling_of_range.isdigit():
    ceiling_of_range = int(ceiling_of_range)
    if ceiling_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")
    quit()
guesses = 0
random_number = random.randint(1, ceiling_of_range)

while True:
    guesses += 1
    player_guess = input("Make a guess: ")
    if player_guess.isdigit():
        player_guess = int(player_guess)
    else:
        print("Please type a number.")
    if player_guess != random_number:
        print("Guess again!")
        if player_guess > random_number:
            print("Lower")
        else:
            print("Higher")
    else:
        print("Congrats you got it!!")
        break

print("It took you", guesses, "guesses")
    
