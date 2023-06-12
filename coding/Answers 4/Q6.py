first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))

nums_sum = first_num + second_num

if  20 >= nums_sum >= 18:
    print("20")
elif 18 > nums_sum >= 15:
    print("18")
elif 15 > nums_sum >= 10:
    print("15")
elif 10 > nums_sum >= 0:
    print("You did not score enough")
else:
    print("Your numbers do not fit")