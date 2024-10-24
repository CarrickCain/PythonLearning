print("Welcome to the DnD quiz!!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay lets begin!!")
score = 0

answer = input("What does AC stand for? ")
if answer.lower() == "armor class":
    print("Nice One!")
    score +=1
else:
    print("Unlucky")

answer = input("What creature usually takes the form of a treasure chest? ")
if answer.lower() == "a mimic":
    print("Nice One!")
    score +=1
else:
    print("Unlucky")

answer = input("what ability allows a fighter to take an extra turn? ")
if answer.lower() == "action surge":
    print("Nice One!")
    score +=1
else:
    print("Unlucky")

answer = input("a god is to a cleric, as a/an ____ is to a warlock? ")
if answer.lower() == "patron":
    print("Nice One!")
    score +=1
else:
    print("Unlucky")
print("You got " + str(score) +"/4 correct!" )
print("You got " + str(score/4 * 100) +"% correct!" )