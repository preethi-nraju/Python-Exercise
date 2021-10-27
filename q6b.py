'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare
them, print out a message of congratulations to the winner, and ask if the players want to start
a new game)
Remember the rules:
 Rock beats scissors
 Scissors beats paper
 Paper beats rock [Topic cover:function]'''

import sys
print("Welcome to the 'rock' 'paper' 'scissors' Game")
rps = ["rock", "paper", "scissors"]
user1 = input("Name of person1: ")
user2 = input("Name of person2: ")

def rock_paper_scissor(input1, input2):
    if (input1 == "rock" and input2 == "scissors") or (input1 == "scissors" and input2 == "paper") or (input1 == "paper" and input2 == "rock"):
        return input1
    elif (input2 == "rock" and input1 == "scissors") or (input2 == "scissors" and input1 == "paper") or (input2 == "paper" and input1 == "rock"):
        return input2

def check_quit(userinput):
    if userinput == "quit":
        print("Thanks for playing. Please visit again!!!")
        sys.exit()

playgame = "yes"

while playgame != "no":
    print("At any time type \"quit\" to quit the game")

    user1_choice = input("What is your choice " + user1 + "? ").lower()
    check_quit(user1_choice)

    while user1_choice not in rps:
        print("Please choose one of the following only: rock, paper, scissor")
        user1_choice = input("What is your choice " + user1 + "? ").lower()
        continue

    user2_choice = input("What is your choice " + user2 + "? ").lower()
    check_quit(user2_choice)

    while user2_choice not in rps:
        print("Please choose one of the following only: rock, paper, scissor")
        user2_choice = input("What is your choice " + user2 + "? ").lower()
        continue

    if user1_choice == user2_choice:
        print("It's a Tie, Please Try again")
    else:
        result = rock_paper_scissor(user1_choice,user2_choice)
        if user1_choice == result:
            print("Congratulations " + user1 + ", you won!")
        else:
            print("Congratulations " + user2 + ", you won!")

    playgame = input("Do you want to play one more game? (yes/no): ")

print("Thanks for playing. Please visit again!!!")