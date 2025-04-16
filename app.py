import random

def guess_the_number():
    """
    A game where the computer tries to guess a number that the user has in mind.
    The user provides feedback (higher/lower) to help the computer guess correctly.
    """
    print("Welcome to the Guess the Number game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    print("After each guess, tell me if your number is 'higher', 'lower', or 'correct'.")
    
    # Initialize variables
    low = 1
    high = 100
    attempts = 0
    
    # Main game loop
    while True:
        # Computer makes a guess
        guess = random.randint(low, high)
        attempts += 1
        
        # Get user feedback
        feedback = input(f"My guess is {guess}. Is your number higher, lower, or correct? ").lower()
        
        # Process feedback
        if feedback == 'correct':
            print(f"Great! I guessed your number in {attempts} attempts.")
            break
        elif feedback == 'higher':
            low = guess + 1
            print("I'll guess higher next time.")
        elif feedback == 'lower':
            high = guess - 1
            print("I'll guess lower next time.")
        else:
            print("Please enter 'higher', 'lower', or 'correct'.")
            attempts -= 1  # Don't count invalid feedback as an attempt
        
        # Check if the range is invalid
        if low > high:
            print("There seems to be an issue with the range. Let's start over.")
            low = 1
            high = 100
            attempts = 0

def main():
    """Main function to run the game."""
    while True:
        guess_the_number()
        
        # Ask if the user wants to play again
        play_again = input("Would you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
