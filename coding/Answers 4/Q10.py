user_num = int(input("Enter a number: "))

result_str = "It can be divided into"

result = 0

if (user_num % 15 == 0) :
    result = result_str + " 15 parts"
elif user_num % 3 == 0:
    result = result_str + " 3 parts"
elif user_num % 5 == 0:
    result = result_str + " 5 parts"
else:
    result = "There is no admission section on either!"

print(result)