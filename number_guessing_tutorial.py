import random 
secret_number = random.randint(1, 1000)

guess = None
attempts = 0 


print("Welcome to the number Guessing Game!")
print("Take a guess between 1-100 and i will tell you if you are right.")


while guess != secret_number:
    guess = int(input("Take a guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Congrats!! You guessed the right number in", attempts, "attempts.")