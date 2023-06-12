Name_of_guests = ["hadis rafati", "kosar rafati", "ana rezaei", "iman sarvarpour", "maryam khaki"]

user_name = input("Enter your name: ")

if user_name.lower() in Name_of_guests:
    print("Welcome♥")
else:
    print("Sorry! you are not a guest")