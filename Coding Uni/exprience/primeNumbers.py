#گرفتن عدد و چاپ اعداد اول قبل از ان

user_number = int(input("Enter Number: "))#7
previous_numbers = list(range(1 , user_number + 1))#1,2,3,4,5,6,7
prime_numbers = []

for per_num in previous_numbers: #5
    flag = 0
    divisor = list(range(2 , per_num)) #2,3,4
    for div in divisor:
        if per_num % div == 0: #درصورت مرکب بودن
            flag += 1
            
        
    if flag < 1:
        prime_numbers.append(per_num)

print(prime_numbers)




#تشخیص عدد اول یا مرکب

# number = int(input("Enter Number: ")) #7
# divisor = range(2 , number) #2,3,4,5,6
# res_com = 0

# for x in divisor:
#     if number % x == 0 :
#         res_com += 1

    
# if res_com > 0 :
#     print(number , "Is Composite number") #مرکب
# else: 
#     print(number , "Is Prime number") #اول
        
