#اعداد اول 0 تا 100

list_of_nums = list(range(100))
list_of_prime_numbers = []

for num in list_of_nums:  #5
    flag = 0
    divisor = range(2 , num)  #2,3,4
    for div in divisor:
        if num % div == 0: #مرکب است
            flag += 1
    
    if flag < 1:
        list_of_prime_numbers.append(num)


for x in list_of_prime_numbers:
    print(x)
