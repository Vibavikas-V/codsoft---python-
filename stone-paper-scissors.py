import random

options = ["stone", "paper", "scissors"]

def play():
    user_wins = 0
    computer_wins = 0
    
    while user_wins < 3 and computer_wins < 3:
        user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            user_wins += 1
            print("You win this round!")
        else:
            computer_wins += 1
            print("Computer wins this round!")
        
        print(f"Score -> You: {user_wins}, Computer: {computer_wins}\n")
    
    if user_wins == 3:
        print("Congratulations! You won the game!")
    else:
        print("Computer wins the game!")

play()
