import random

def guess_the_number():
    print("🎲 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("🚫 Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
