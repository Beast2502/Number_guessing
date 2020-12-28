import random 


guess = []


myComputer  = random.randint(1,70)
player = int(input("Enter a number between 1 to 70 => "))


while player !=myComputer:
    if player > myComputer:
        print("Number is too high")
    else:
        print("Number is too low")
    player = int(input("Enter a number between 1-70 => "))
    guess.append(player)
 
else:
    print("You Have gussed right.Good job!!")
    print(f"It took you {len(guess)} guesses")
    print("These were your guesses")
    print(guess)