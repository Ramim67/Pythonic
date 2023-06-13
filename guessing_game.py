import random

print("Welcome to the guessing game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Allow the user to make up to 5 guesses
for i in range(5):
    # Get the user's guess
    guess = int(input("Enter a guess between 1 and 10: "))
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed the correct number!")
        break
    elif guess < secret_number:
        print("Your guess was too low. Try again.")
    else:
        print("Your guess was too high. Try again.")

# If the user didn't guess the number after 5 tries, inform them that they lost
if guess != secret_number:
    print("Sorry, you lost. The secret number was", secret_number)