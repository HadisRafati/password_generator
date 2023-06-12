#خروجی نادرست میده

i = 1
index = 0

user_name1 = 0
user_age1 = 0
user_work1 = 0

user_name2 = 0
user_age2 = 0
user_work2 = 0

user_name3 = 0
user_age3 = 0
user_work3 = 0

variable_list = [user_name1, user_age1, user_work1,
 user_name2, user_age2, user_work2,
user_name3, user_age3, user_work3]


while i <= 3:
    variable_list[index] = input(f"Enter user name{i}:")
    if variable_list[index] == '':
        print("It is empty!")
        continue
    index += 1

    variable_list[index] = int(input(f"Enter user age{i}:"))
    if variable_list[index] == '':
        print("It is empty!")
        continue
    index += 1

    variable_list[index] = input(f"Enter user work{i}:")   
    if variable_list[index] == '':
        print("It is empty!")
        continue
    index += 1
    i += 1

flag = 1

user_info = [(user_name1, user_age1, user_work1),
 (user_name2, user_age2, user_work2), 
(user_name3, user_age3, user_work3)]

variable_list == user_info

while flag < 4:
    for (user_name, user_age, user_work) in user_info:
        print(print(f" user{flag} =\n name is {user_name}, age is {user_age}, work is {user_work}"))
        flag += 1