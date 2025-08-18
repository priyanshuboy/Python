import random

choices = ['rock', 'paper', 'scissors']
running = True
UserScore = 0
ComputerScore = 0

while running:
    UserChoice = input("Enter your choice (rock/paper/scissors): ").lower()
    ComputerChoice = random.choice(choices)
    print(f"Computer chose: {ComputerChoice}")

    if UserChoice == ComputerChoice:
        print("Tie!")

    elif UserChoice == "rock" and ComputerChoice == "paper":
        print("You lose!")
        ComputerScore += 1
    elif UserChoice == "rock" and ComputerChoice == "scissors":
        print("You win!")
        UserScore += 1

    elif UserChoice == "paper" and ComputerChoice == "rock":
        print("You win!")
        UserScore += 1
    elif UserChoice == "paper" and ComputerChoice == "scissors":
        print("You lose!")
        ComputerScore += 1

    elif UserChoice == "scissors" and ComputerChoice == "rock":
        print("You lose!")
        ComputerScore += 1
    elif UserChoice == "scissors" and ComputerChoice == "paper":
        print("You win!")
        UserScore += 1
    else:
        print("Invalid choice! Please choose rock, paper, or scissors.")


    end = input("Do you want to play again? (y/n): ").lower()
    if end != "y":
        running = False

print("Final Scores:")
print("Your score =", UserScore, " Computer score =", ComputerScore)

