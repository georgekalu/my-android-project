import random

print("🎲 Number Guessing Game")
print("======================\n")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess it.\n")

secret = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts+1}/{max_attempts} - Enter your guess: "))
        
        attempts += 1
        
        if guess < secret:
            print("Too low! Try higher.")
        elif guess > secret:
            print("Too high! Try lower.")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
            print(f"The number was {secret}.")
            break
    except ValueError:
        print("Please enter a valid number!")

if attempts == max_attempts and guess != secret:
    print(f"\n😔 Game over! The number was {secret}.")

print("\nThanks for playing! 💪")
