'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start
a new game)
Remember the rules:
 Rock beats scissors
 Scissors beats paper
 Paper beats rock'''

again = 'yes'
while (again == 'yes'):

    p1 = input("Player 1 --> Rock, Paper, or Scissors? ")
    p1 = p1.lower()
    print()

    p2 = input("Player 2 --> Rock, Paper, or Scissors? ")
    p2 = p2.lower()
    print()

    if (p1 == "rock"):
        if (p2 == "rock"):
            print("The game is a tie")
        elif (p2 == "paper"):
            print("Player 2 wins!")
        elif (p2 == "scissors"):
            print("Player 1 wins!")
    elif (p1 == "paper"):
        if (p2 == "rock"):
            print("Player 1 wins!")
        elif (p2 == "paper"):
            print("The game is a tie")
        elif (p2 == "scissors"):
            print("Player 2 wins!")
    elif (p1 == "scissors"):
        if (p2 == "rock"):
            print("Player 2 wins!")
        elif (p2 == "paper"):
            print("Player 1 wins!")
        elif (p2 == "scissors"):
            print("The game is a tie")
    else:
        print("Invalid input, try again")

    again = input("Type yes to play again, anything else to stop: ")
    print()