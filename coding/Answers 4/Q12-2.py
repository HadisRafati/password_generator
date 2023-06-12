user_name = input("Enter the user name: ")

flag = 0  #روش flag

len_name = len(user_name)

if len_name < 4:
    print("Tol Username hadaghal az 4 character bishtar bashad") 
    flag = 1  #flag روش

#####

user_pass = input("Enter the password: ")

len_pass = len(user_pass)

if len_pass < 8:
    print("Password nabayad az 8 character kochektar bashad")
    flag = 1

if len_pass > 20:
    print("Password nabayad bozorgtar az 20 character bashad")
    flag = 1

if user_name == user_pass:
    print("Username and Password mosavi")
    flag = 1

# if(len_pass > 8) and (len_pass < 20) and (len_name > 4) and (user_name != user_pass):
#     print("Vorodi ha dorost bodeh✓ \nUsername and Password save shod")  #روش خودم

# if not (len_name < 4) or (len_pass < 8) or (len_pass > 20) or (user_name == user_pass):
#     print(f"Username: {user_name} \nPassword: {user_pass}")    روش استاد


if flag == 0:
     print(f"Username: {user_name} \nPassword: {user_pass}")  #روش flag