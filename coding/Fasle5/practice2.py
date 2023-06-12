import random

number_of_cups = int(input("How many cups? "))
number_of_guess = int(input("How many chances? "))

LINE_LENGHT = "-" * 20
print(LINE_LENGHT)

if (number_of_cups // 2) > number_of_guess:
    print("Game level: Hard")
elif(number_of_cups // 2) < number_of_guess:
    print("Game level: Easy")
else:
    print("Game level: Medium")
    

goal_cup = random.randint(1 , number_of_cups)

word = 's'

for guess in range(number_of_guess):

    
    if (number_of_guess - guess) == 1:
        word = ''

    print(f"{number_of_guess - guess} Chance{word} left.")

    user_guess = int(input(f'Guess [1-{number_of_cups}]: '))

    if user_guess == goal_cup:
        print("You guessed right")
        print(LINE_LENGHT)
        print("You won!")
        break

    else:
        print("Wrong guess.")
        print(LINE_LENGHT)
        # number_of_guess -= 1

        if (guess + 1) == number_of_guess:
            print(f"The right answer is {goal_cup}")
            print("You lost. Sorry!")
        

