import random

number_to_be_guessed = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))

if guess == number_to_be_guessed:
    print("you got it right")
else:
    print("Try again later, its unfortunate you could not guess", number_to_be_guessed)
