user_num = int(input("Enter a number: "))

result = 1


for i in range(2 , user_num):
    if user_num % i == 0:
        result = 0
        print(f"{user_num} % {i} ")
        break
        
    

if result == 1:
    print(f"{user_num} is prime number.")
elif result == 0:
    print(f"{user_num} is not prime number.")