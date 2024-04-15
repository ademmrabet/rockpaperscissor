import random

userWins = 0 
computerWins = 0
draws = 0
choices = ["rock", "paper", "scissors"]
while True:
    user_input = input("Choose Rock, Paper or Scissors and Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        continue

    randomNumber = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computerGuess = choices[randomNumber]
    print("Computer guess: ", computerGuess + ".")

    if user_input == "rock" and computerGuess == "scissors":
        print("You won!")
        userWins += 1

    elif user_input == "scissors" and computerGuess == "paper":
        print("You won!")
        userWins += 1

    elif user_input == "paper" and computerGuess == "rock":
        print("You won!")
        userWins += 1

    elif user_input == computerGuess:
        print ("That's a draw!")
        draws += 1
    else:
        print("You lost :(")
        computerWins += 1

print("You won", userWins, "Times")
print("You lost", computerWins, "Times")
print("and this game had", draws, "draws")
print("Goodbye!")
    
