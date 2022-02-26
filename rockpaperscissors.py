from http.client import CONTINUE
import random

choices = ['rock', 'paper', 'scissors']
score = 0
games = 0  # the number of games we are currently playing will increase

print("Let's Play Rock Paper Scissors!")


def actualGame(games, score, choices):
    while games < 3:  # we will play 3 games
        # Here I will set it up for user input and change whatever input that is to lower
        userInput = input(
            "Choose one of the following choices: \n Rock, Paper or Scissors: ")
        userChoice = userInput.lower()
        computerChoice = random.choice(choices)
        # end
        if userChoice == computerChoice:
            print("Tie! Let's try that again")
            games = games + 1
            continue
        elif (userChoice == "rock" and computerChoice == "scissors") or (userChoice == "paper" and computerChoice == "rock") or (userChoice == "scissors" and computerChoice == "paper"):
            games = games + 1
            score = score + 1
            print("You win this round!")
            continue
        elif (computerChoice == "rock" and userChoice == "scissors") or (computerChoice == "paper" and userChoice == "rock") or (computerChoice == "scissors" and userChoice == "paper"):
            games = games + 1
            print("Computer wins this round!")
        else:
            print("Invalid input. Please try again")
            continue

    print("Your score: {}. Thanks for playing!".format(str(score)))


actualGame(games, score, choices)
# Asking the user if they want to play again

playAgainQuestion = input("Would you like to play again? Press y or n. ")
userResponse = playAgainQuestion.lower()
while True:
    if userResponse == "y":
        actualGame(games, score, choices)
        break
    elif userResponse == "n":
        print("The game is over. Thanks for playing!")
        break
    else: 
        userResponse = input("I don't recognize that reponse. Do you want to play again? y or n: ")
        pass
