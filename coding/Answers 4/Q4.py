number_a = int(input("Enter the first number: "))
number_b = int(input("Enter the second number: "))

choice = ["+","-","*"]

user_choice = input(f"Enter one of the words: => (+, -, *)\n")

if user_choice == choice[0]:
    print("Result:",number_a + number_b)
elif user_choice == choice[1]:
    result = number_a - number_b
    print("Result:",result)
elif user_choice == choice[2]:
    result = number_a * number_b
    print("Result:",result)

elif user_choice == 'nemikham':
    x = int(input("enter: "))
    if x > 100:
        print("bozorge")
    else:
        print("kochike")

else:
    print("The entered word is invalid.")
 