weight = float(input("What is your weight: "))
lb_kg = str(input("Is this in lb's or kgs? "))

if(lb_kg.lower() == "lb"):
    print("This is your weight in kg's:", weight/2.205)
elif(lb_kg.lower() == "kg"):
    print("This is your weight in lb's:", weight*2.205)
else:
    print("Error try again")
 
