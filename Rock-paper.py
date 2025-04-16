import random

def play_game():
    # List of possible choices
    choices = ["rock", "paper", "scissors"]
    
    # Get user's choice
    user_choice = input("What do you choose? Type 'rock', 'paper', or 'scissors': ").lower()
    
    # Validate user input
    if user_choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        return
    
    # Get computer's choice
    computer_choice = random.choice(choices)
    
    # Print choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("--------------------------------")
    
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
