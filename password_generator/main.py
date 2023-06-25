import random
import string
#بهینه سازی و تحلیل کد*****************
def welcome_message():
    print('='*51,"\n Welcome to the Random Password Generator program.\n",'='*51 ,sep= '')
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
    



list_of_settings_funcs = [func_upper_case, func_lower_case, func_symbol, func_number, func_space]

def re_creat_password_old_settings(length_pass_user, upper_case_user, lower_case_user, symbol_user, number_user, space_user):

    input_user = input("Enter '1' if you want to Creating a password with new settings, \nEnter '2' if you want to Creating a password with old settings, \nEnter '0' if you want to exit: ").lower()

    print()
    if input_user == '2':
        creat_password(length_pass_user, upper_case_user, lower_case_user, symbol_user, number_user, space_user)

    elif input_user == '0':
        print("Goodbye My friend!")
    
    elif input_user == '1':
        user_inputs()




def creat_password(length_pass_user, upper_case_user, lower_case_user, symbol_user, number_user, space_user): #بود یا نبود تنطیمات رو به هم وصل میکنه و استرینگ پسورد رو برمیگردونه
    
    list_pass = [] #["", "","","", ""]
    list_of_user_settings = [upper_case_user, lower_case_user, symbol_user, number_user, space_user]


    index_setting = list(range(len(list_of_user_settings))) #[0,1,2,3,4]
    
    
    for i in range(length_pass_user):#5

        rand_set = random.choice(index_setting) #2
        index_setting.remove(rand_set) #[0,1,3,4]
        index_setting.insert(0, rand_set)
    
    
        for y in index_setting:
            if len(list_pass) < length_pass_user:
                if list_of_user_settings[y] == "yes":
                    list_pass.append(list_of_settings_funcs[y]())


    
                    
    password = ''.join(list_pass) #lsit to string password
    print("\nYour password is: " + password, "\n", '-'*40)

    re_creat_password_old_settings(length_pass_user, upper_case_user, lower_case_user, symbol_user, number_user, space_user)


def user_inputs():
    input_defult = {"y" : "yes", "n" : "no", "lenght" : "8"}
    length_pass_user = 8
    upper_case_user = "yes"
    lower_case_user = "yes"
    symbol_user = "yes"
    number_user = "yes"
    space_user = 'no'



    dict_of_sets = {'upper_case_user' : "upper case",
     "lower_case_user": "lower case", 
     "symbol_user" : "sumbol",
      "number_user" : "number",
       "space_user" : "space"}
    
    list_of_sets = [[upper_case_user, "yes"], [lower_case_user , "yes"]]

    z = 0
    
    for key, value in dict_of_sets.items():

        dict_of_sets[key] =  input(f"Do you want to use '{list(dict_of_sets.values())[z]}' in the password? [*enter-> option = {input_defult['y']}] ") or i
        

        z+=1

    print(dict_of_sets)
   

    


    creat_password(int(length_pass_user), upper_case_user, lower_case_user, symbol_user, number_user, space_user)



        

welcome_message()