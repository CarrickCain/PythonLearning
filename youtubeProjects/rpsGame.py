import random

user_score = 0
computer_score = 0
draws = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Enter rock/paper/scissors or Q to quit ")

    if user_input.lower() == "q":
        break
    if user_input not in options:
        continue
    random_num = random.randint(0,2) # rock: 0, paper: 1, scissors: 2 
    computer_pick = options[random_num]
    print("The computer picked", computer_pick + ".")

    if computer_pick == "rock" and user_input =="paper":
        print("You win!!")
        user_score+=1
    elif computer_pick == "paper" and user_input =="scissors":
        print("You win!!")
        user_score+=1
    elif computer_pick == "scissors" and user_input =="rock":
        print("You win!!")
        user_score+=1
    elif computer_pick == user_input:
        print("Its a draw!!")
        draws+=1
    else:
        print("You lose!")
        computer_score+=1

print("You won",user_score, "times!!")
print("The computer won", computer_score, "times!!")
print("There were", draws, "draws!!")
print("Thanks for playing!!")