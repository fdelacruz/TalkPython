import random

print("----------------------------------------------")
print("              GUESS THE NUMBER GAME           ")
print("----------------------------------------------")
print()

random_number = random.randint(0, 100)

guess = -1
while guess != random_number:
    guess = int(input("Guess a number between 0 and 100: "))

    if guess > random_number:
        print(f"Sorry {guess} was too HIGH")
    elif guess < random_number:
        print(f"Sorry {guess} was too LOW")
    else:
        print(f"YES, you got it! The number was {random_number}")
