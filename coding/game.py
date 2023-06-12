#به صورتی که هرکی زودتر به امتیاز 5 رسید

import random


choice = ["r", "p", "s"]
user_choice = {
    'r' : "Rock",
    "p" : "Paper",
    "s" : "Scissor"
}
user_score = 0
ai_score = 0
final_number = 5

while True:

    user_input = (input("Enter your choice (R, P, S): ")).lower()
    ai_choice = random.choice(choice)


    if user_input in choice:
        print(f"User choice= {user_choice[user_input]} \nAi choice= {user_choice[ai_choice]}")

        if user_input == ai_choice:
            print("Tie")

        elif (user_input == 'r') and (ai_choice == "s"):
            print("User +1")
            user_score += 1

        elif (user_input == 'p') and (ai_choice == 'r'):
            print("User +1")
            user_score += 1

        elif (user_input == 's') and (ai_choice == 'p'):
            print("User +1")
            user_score += 1

        else:
            print("Ai +1")
            ai_score += 1
         
    else:
        print("Invalid input")
        
    
    print(f'User score= {user_score}, Ai score= {ai_score}')
    print("\n", "_"*15, '\n')
    
    if user_score  == final_number or ai_score == final_number :
        break


print(f"User score= {user_score}, Ai score= {ai_score}")


if user_score == final_number:
    print("Winner is User.")
else:
    print("Winner is Ai.")









#به صورتی که تا تعداد 5 هرکی بیشتر امتیاز اورد
# import random

# choice = ["r", "p", "s"]
# user_choice = {
#     'r' : "Rock",
#     "p" : "Paper",
#     "s" : "scissor"
# }
# user_score = 0
# ai_score = 0
# i = 0

# while i < 5:

#     user_input = (input("Enter your choice (R, P, S): ")).lower()
#     ai_choice = random.choice(choice)


#     if user_input in choice:
#         print(f"User choice= {user_choice[user_input]} \nAi choice= {user_choice[ai_choice]}")

#         if user_input == ai_choice:
#             print("Tie")

#         elif (user_input == 'r') and (ai_choice == "s"):
#             print("User +1")
#             user_score += 1

#         elif (user_input == 'p') and (ai_choice == 'r'):
#             print("User +1")
#             user_score += 1

#         elif (user_input == 's') and (ai_choice == 'p'):
#             print("User +1")
#             user_score += 1

#         else:
#             print("Ai +1")
#             ai_score += 1

#     else:
#         print("Invalid input")
#         i -= 1  #استاد
#         #continue خودم
    
#     print(f'User score= {user_score}, Ai score= {ai_score}')
#     print("\n", "_"*15, '\n')
#     i += 1

# print(f"User score= {user_score}, Ai score= {ai_score}")

# if user_score > ai_score:
#     print("Winner is User.")
# elif user_score < ai_score:
#     print("Winner is Ai.")
# else:
#     print(f"You are Tie.")