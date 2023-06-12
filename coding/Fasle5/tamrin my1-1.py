#بعد از خالی وارد کردن دوباره از کاربر اول شروع میکنه و تعداد تکرار بالاست

i = 1     

while i == 1:
    user_name1 = input(f"Enter user name{i}:")
    if user_name1 == '':
        print("It is empty!")
        continue

    user_age1 = int(input(f"Enter user age{i}:"))

    user_work1 = input(f"Enter user work{i}:")
    if user_work1 == '':
        print("It is empty!")
        continue
    i += 1
##############
    user_name2 = input(f"Enter user name{i}:")
    if user_name2 == '':
        print("It is empty!")
        i -= 1
        continue

    user_age2 = int(input(f"Enter user age{i}:"))

    user_work2 = input(f"Enter user work{i}:")
    if user_work2 == '':
        print("It is empty!")
        i -= 1
        continue
    i += 1

    user_name3 = input(f"Enter user name{i}:")
    if user_name3 == '':
        print("It is empty!")
        i -= 1
        continue

    user_age3 = int(input(f"Enter user age{i}:"))

    user_work3 = input(f"Enter user work{i}:")
    if user_work3 == '':
        print("It is empty!")
        i -= 1
        continue
    i += 1


flag = 1

    
user_info = [(user_name1, user_age1, user_work1),
 (user_name2, user_age2, user_work2), 
(user_name3, user_age3, user_work3)]


while flag < 4:
    for (user_name, user_age, user_work) in user_info:
        print(f" user{flag} =\n name is {user_name}, age is {user_age}, work is {user_work}")
        flag += 1