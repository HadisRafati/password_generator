def print_star_line(number_of_star, total_star):
    number_of_spaces = (total_star - number_of_star) //2
    print(' ' * number_of_spaces, end='')
    print('*' * number_of_star, end='')
    print(' ' * number_of_spaces)

def draw_diamond(num):
    print()
    number_of_star = None
    for i in range(num):
        if i < num / 2:
            number_of_star = i * 2 + 1
        else:
            number_of_star = (num - i) * 2 - 1
        
        print_star_line(number_of_star , num)

def get_input():
    while True:
        user_num = int(input('Enter the odd number: '))
        if user_num % 2 != 0:
            return user_num

        print('Error. This number is even')
        change_even_num = int(input('Change even number to odd (1)\nRe-enter the number (2)\n'))
        if change_even_num == 1:
            user_num += 1
            return user_num


draw_diamond(get_input())