import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0

    while guess != random_number:
        guess = int(input("number: "))

        if guess < random_number:
            print("guess number is too low")
        elif guess > random_number:
            print("guess number is too high")
    print(f"YaY!! the number{guess} is the right Guess")

guess(5)
