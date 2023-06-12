import random

currect_word = ''

def enter_list_of_words():
    list_of_words = []

    while True:
        user_word = (input('Enter some words and start the game by entering "done": ')).lower()

        if user_word == "done":
            print("-"*20)
            break

        list_of_words.append(user_word)

    return list_of_words


def welcome(number_of_round):
    print("Welcome to the guess the words.")
    print(f"You have to choose a word from the list and you have up to {number_of_round} chances.\n" ,"-"*20)

def ai_choose(list_of_words):
    right_word = random.choice(list_of_words)
    return right_word

def user_choose(list_of_words):
    j = 0

    while j == 0:
        
        user_word = input("Enter the selected word: ").lower()

        if user_word.isalpha():
            return user_word

        print("Please enter only one word and only letters a-z\n", "-"*20)
        

def end_of_the_game(number_of_first_round):
    print("-"*20)
    user_input = int(input("Do you want to play again? \n(1: Play Again , 2: Exit): "))
    print("-"*20)
    if user_input == 1:
        global list_of_words
        list_of_words = []
        list_of_words = enter_list_of_words() #لیست جدید
        global currect_word
        currect_word = ai_choose(list_of_words)#کلمه ی جدیدی برمیداره
        tpl_for_return = (number_of_first_round, list_of_words)
        return tpl_for_return
    else:
        print("Bye")
        return 0



def run_game(number_of_round, list_of_words): #تابع اصلی
    
    number_of_first_round = number_of_round
    welcome(number_of_round)
    global currect_word
    currect_word = ai_choose(list_of_words) 
    
    while number_of_round != 0:
        print(list_of_words)
        user_word = user_choose(list_of_words)
        
        if user_word in list_of_words:
            if user_word == currect_word: #ورودی درست
                print("You made the right choice.")
                number_of_round,list_of_words = end_of_the_game(number_of_first_round)
                
            elif number_of_round != 1:
                print(f"Your chose wrong. \nTry again.Number of rounds left:{number_of_round-1} \n", "-"*20)
                number_of_round -= 1

            elif number_of_round == 1: #آخرین حدس
                print("Your chose wrong. \nYou lost.")
                number_of_round -= 1
                print(f"Currect word: {currect_word}") #چاپ کلمه درست
                number_of_round,list_of_words = end_of_the_game(number_of_first_round) #خروج یا بازی دوباره
                

        else:
            print("Your choose not in list of word.\n", "-"*20)


list_of_words = enter_list_of_words()
run_game(2, list_of_words)