# import random
# list_of_word = ['hello', 'hi', 'sun', 'father', 'bag', 'today', 'coding', 'line', 'pencel', 'water']

# selected_word = random.choice(list_of_word)

# flag = 5
# def print_game_help():
#     print('-'*15)
#     print(f'You have {flag} guesses to guess the selected word from the list below.')
#     print(f'list of words = {list_of_word}.')
#     print('-'*15)

# def get_input():
#     print('\nWelcome to the *Words Game*')
    
#     global flag
#     while flag > 0:
#         print_game_help()
#         user_input = (input('Enter your guess: ').lower())

#         if (user_input.isalpha()):
#             flag -= 1
#             if flag == 0:
#                 continue
            
#             if user_input == selected_word:
#                 print('Very good\nYour guess is true')
#                 return 

#             print('Please try again.')
            
#         else:
#             print('Your input was not correct. Please Enter again.')
        
#         print('')
#     print(f'\nYou are lose!\n"{selected_word}" is selected.')

# get_input()











import random

def print_game_intro():
    print('-'*15)
    print('Welcome to the *word game*')
    print(f'List all words: {list_of_words}')
    print('Please start guessing.')
    print('-'*15)

def get_input():
    while True:
        user_guess = input('\nEnter the guess: ').lower()
        if user_guess.isalpha():
            return user_guess

        print('Your input was not correct. \nPlease try again.')

def check_input_in_list(word):
    user_guess = get_input()

    while user_guess not in word:
        print("Your input is not in the list.")
        print('Please try again.')
        user_guess = get_input()

    return user_guess

def run_game(number_of_round, word):
    correct_word = random.choice(word)
    print_game_intro()

    print(f'Number of guessing: {number_of_round}')
    
    for i in range(number_of_round):
        user_input = check_input_in_list(word)
        if user_input == correct_word:
            print('Thats right!')
            print('You WON!!!')
            return
        elif i != number_of_round - 1:
            print('OH. Please try again.')
            print('-'*15)
            print(f'Number of guesses left: {number_of_round-1 -i}')
            print('-'*15)
    print("Oo. I'm sorry!")
    print('You LOSE!')
    print(f'Correct word is: {correct_word}')

list_of_words = ['hello', 'hadis', 'hi', 'red', 'bag', 'pencil', 'book', 'sun', 'keyboard']
run_game(5, list_of_words)