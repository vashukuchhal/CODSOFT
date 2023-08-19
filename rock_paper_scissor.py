import random
import os

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        user_choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    if user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    if user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        
        print(f"Your score: {user_score} | Computer's score: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    os.system('cls')
    play_game()
