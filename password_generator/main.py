import os
import random
import string
##  تغییر اسم متغیر ها و تمییز نویسی کزدن


def welcome_message():
    os.system('cls') #clear screen

    print('='*51,"\n Welcome to the Random Password Generator program." ,sep= '')
    print("\n",'_' * 10,"Developer: Hadis Rafati" ,'_' * 10)
    print(" " * 6, "Email: hadisrafati813@gmail.com\n", '='*51, "\n")

    user_inputs()



def func_upper_case():
    upper_case = random.choice(string.ascii_uppercase)
    return upper_case


def func_lower_case():
    lower_case = random.choice(string.ascii_lowercase)
    return lower_case



def func_symbol():
    symbol = random.choice(string.punctuation)
    return symbol
    

def func_number():
    number = random.choice(string.digits)
    return number
    

def func_space():
    return " "
    



funcs_to_apply_settings = [func_upper_case, func_lower_case, func_symbol, func_number, func_space]

def re_generate_password(length_pass, upper_case, lower_case, symbol, number, space):

    defult_setting = "Generate password with old settings"
    user_input = input("Enter '1' if you want to generating a password with new settings,"            #show this str after generate password.
                       "\nEnter '2' if you want to generating a password with old settings,"
                       f"\nEnter '0' if you want to exit \n[*enter-> defult: {defult_setting}]: ").lower() or "2"

    print()
    if user_input == '2':
        generate_password(length_pass, upper_case, lower_case, symbol, number, space)

    elif user_input == '0':
        print("Goodbye My friend!") #exit
    
    elif user_input == '1':
        user_inputs()




def generate_password(length_pass, upper_case, lower_case, symbol, number, space): #
    
    list_of_generated_pass = [] #["", "","","", ""]
    list_of_pass_settings = [upper_case, lower_case, symbol, number, space]


    indexes_of_list_of_settings = list(range(len(list_of_pass_settings))) #[0,1,2,3,4]
    
    #*********************************************************************
    while len(list_of_generated_pass) < length_pass:
        for i in range(length_pass):#8  #Random selection of settings

            radomize_option = random.choice(indexes_of_list_of_settings) #2 
            
            indexes_of_list_of_settings.remove(radomize_option) #[0,1,3,4]
            indexes_of_list_of_settings.insert(0, radomize_option) #[2,0,1,3,4]
        
        for y in indexes_of_list_of_settings:
            if len(list_of_generated_pass) < length_pass:
                if list_of_pass_settings[y] == "yes":
                    list_of_generated_pass.append(funcs_to_apply_settings[y]())

    #*********************************************************************
    
                    
    password = ''.join(list_of_generated_pass) #convert password list to string
    print("\nYour password is: " + password, "\n", '-'*40)

    re_generate_password(length_pass, upper_case, lower_case, symbol, number, space)


MIN_PASSWORD_LENGTH = 4
MAX_PASSWORD_LENGTH = 30

def set_length_pass_user(min_password_length, max_password_length):
    defult_password_length = "8"

    j = 1
    while j == 1:
        length_pass = input(f"Enter password length [*enter-> defult: {defult_password_length}]: ") or defult_password_length 

        if length_pass.isnumeric():
            
            if min_password_length <= int(length_pass) < max_password_length:
                j = 0
                return length_pass
            else:print(f"Invalid input. Length of password beetwen {min_password_length} and {max_password_length}.\n")

        else: print("Invalid input. Please enter only digit.\n")



def user_inputs():
    
    dict_for_show_and_get_settings = {
        "upper case" : "yes",
        "lower case": "yes", 
        "symbol" : "yes",
        "number" : "yes",
        "space" : 'no'}
    

    length_pass = set_length_pass_user(min_password_length = MIN_PASSWORD_LENGTH, max_password_length = MAX_PASSWORD_LENGTH) #get password length

    for option, defult in dict_for_show_and_get_settings.items(): #show and getting settings

        while True:
            dict_for_show_and_get_settings[option] =  (input(f"Do you want to use '{option}' in the password?" 
                                                     f"[*enter-> defult : {defult}] ")).lower() or defult

            if dict_for_show_and_get_settings[option] in ['yes', "no"]: #Checking the correctness of user inputs
                break

            else:
                print("Invalid input. Please enter 'Yes' or 'No'\n")

            
    upper_case = dict_for_show_and_get_settings["upper case"]
    lower_case = dict_for_show_and_get_settings["lower case"]
    symbol = dict_for_show_and_get_settings["symbol"]
    number = dict_for_show_and_get_settings["number"]
    space = dict_for_show_and_get_settings["space"]
           

    generate_password(int(length_pass), upper_case, lower_case, symbol, number, space)


welcome_message()