import random

def get_input():
    while True:
        user_input = (input('\nEnter your guess: ').lower())
        if user_input.isalpha():
            return user_input
        print('Your input was not correct. Please Enter again.')

def get_input_from_list(words):        
    user_input = get_input()
    while user_input not in words:
        print('You should guess a word from the given words list')
        print('Please enter the correct word.')
        user_input = get_input()
    return user_input

def print_game_intro():
    print('-'*15)
    print('Welcome to the *Words Game*')
    print(f'list of words = {list_of_word}.')
    print('please start guessing')
    print('-'*15)


def run_game(number_of_rounds, words):
    print_game_intro()

    print(f'Number of guessing: {number_of_rounds}')
    correct_word = random.choice(words) 
    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)

        if user_input == correct_word:
            print('YOU WON')
            return
        else:
            print('You guessed wrong!')
            print(f'Please try again! Number of rouns left: {number_of_rounds-1-i}')
    print('YOU LOSE')
    
list_of_word = ['hello', 'hi', 'sun', 'father', 'bag', 'today', 'coding', 'line', 'pencel', 'water']
run_game(5, list_of_word)