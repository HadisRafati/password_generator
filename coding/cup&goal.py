import random as rand

number_of_cup = int(input("Enter the number of Cup: "))
number_of_guess = int(input("Enter the number of guesses:"))
print("------------------------")

list_of_cup = range(1, number_of_cup+1) #لیست لیوان ها

cup_of_goal = rand.choice(list_of_cup) #لیوان دارای گل

if number_of_cup > number_of_guess:

    for x in range(number_of_guess):
        if 0 < number_of_guess:
            print(f"{number_of_guess} Chances left.")
            user_guess = int(input(f"Guess [1-{number_of_cup}]: "))
            if cup_of_goal == user_guess:
                print("You guessed Right.\n------------------------")#حدس درست
                number_of_guess -= 1
                break

            elif user_guess not in list_of_cup:#نامعتبر
                print("Invalid input.\n------------------------")

            else:#حدس اشتباه
                print("Wrong Guess.\n------------------------")
                number_of_guess -= 1
                if 0 == number_of_guess:
                    print("You Lost.")
                    print(f"correct guess: {cup_of_goal}")
                    
else:
    print("The number of glasses should be more than the number of guesses!")
            