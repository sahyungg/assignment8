def playerGuess():

    import random

    guess = str(input("Guess the number: "))

    answer = str(random.randrange(0, 100))

    if guess > answer:
        print(f"{guess} is greater than {answer}.")
    elif guess == answer:
        print("The number you have guessed is equal to the answer.")
    else:
        print(f"{guess} is less than {answer}.")

    if guess != answer:
        print("try again")
        playerGuess()
    elif guess == answer:
        print("You got it right!")

playerGuess()