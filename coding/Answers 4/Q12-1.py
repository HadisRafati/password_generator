user_name = input("Enter the user name: ")
user_pass = input("Enter the password: ")

len_name = len(user_name)
len_pass = len(user_pass)

Result = 0

if user_name == user_pass:
    Result = "Username and Password mosavi"
elif len_pass < 8:
    Result = "Password nabayad az 8 character kochektar bashad"
elif len_pass > 20:
    Result = "Password nabayad bozorgtar az 20 character bashad"
elif len_name < 4:
    Result = "Tol Username hadaghal az 4 character bishtar bashad"
else:
    Result = "Vorodi ha dorost bodeh✓ \nUsername and Password save shod"

print(Result)