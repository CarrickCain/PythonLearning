'''
---My Mockup code---

have the user roll a dice with numbers between 1-6
score = 0
current_score = 0
while True:
    input(would you like to roll? (roll/stop))
    #if input == roll:
        rolled_num = random_number gen (1-6)
            if rolled_num == "1":
                break
                print(you lose)
        current_score += rolled_num
    elif input == stop
        score += current_score 
        print("your current score is",score)
    elif input == "q":
        break
    else:
        print(invalid, try again)
'''
# my firt attempt at the pig game 
import random

#returns a random number from 1-6 to simulate a six-sided die roll
def roll():
    min_num = 1
    max_num = 6
    rolled_num = random.randint(min_num,max_num)
    return rolled_num

while True:
    players = input("How many people are playing?(2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("You have",players,"players")
            break
        else:
            print("Must be from 2-4")
    else:
        print("Please enter a number from 2-4")

max_score = 50
player_scores = [0 for _ in range(players)]
# current_score = 0

while max(player_scores) < max_score:
    for player_index in range(players):
        print("\nPlayer number", player_index + 1, "your turn has started")
        print("Your total score is:",player_scores[player_index],"\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != "y": 
                break
            
            value = roll()

            if value == 1:
                print("Oops you rolled a 1, turn over")
                current_score = 0
                break
            else:
                current_score += value
                print("you rolled a", value)
            print("Your current score is:", current_score)
        player_scores[player_index] += current_score
        print("Your total score is:", player_scores[player_index])
max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player number", winning_index + 1,
      "is the winner with a score of",max_score)




# while True:
#        user_input = input("Would you like to roll or stop rolling? (roll/stop). Press q to quit ").lower()
#        if user_input == "roll":
#            rolled = roll()
#            if rolled == 1:
#               print("woops you rolled a",rolled,"you lose")
#               break
#            current_score += rolled
#            print(current_score)
#        elif user_input == "stop":
#            score = current_score
#            print("Your current score is", score)
#        elif user_input == "q":
#            break
#        else:
#            print("Invalid command. Try again")
       