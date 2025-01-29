import random

def number_guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 5
    
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("Guess the number between 1 and 20. You have 5 attempts.")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))
            
            if guess < 1 or guess > 20:
                print("Please enter a number between 1 and 20.")
                continue
            
            if guess == number_to_guess:
                print("🎉🎉 Congratulations! You did it! 🎉🎉")
                print(f"You guessed the number in {attempt} attempts! You're a champion! 🏆")
                return
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    print(f"Good effort! The correct number was {number_to_guess}. Keep practicing, and you'll get it next time! 🚀")

# Run the game
number_guessing_game()