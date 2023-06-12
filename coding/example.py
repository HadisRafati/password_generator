#رسم لوزی

def calc_diamond(diameter_of_diamond):
    #ex: 7
    if diameter_of_diamond % 2 != 0: #valid input

        list_of_number_stars = []
        for x in range(1, diameter_of_diamond): #ردیف های ستاره در لوزی
            if x % 2 != 0:
                list_of_number_stars.append(x) 
        

        list_of_spaces = []
        for x in range(1, (diameter_of_diamond//2)+1): #تعداد اسپیس های پشت ستاره ها
            list_of_spaces.append(x) #ex: 1,2,3
        
        draw_diamond(list_of_number_stars, list_of_spaces, diameter_of_diamond)
    else: print("Error: The input number must be odd")#invalid input



def draw_diamond(list_of_number_stars, list_of_spaces, diameter_of_diamond):

    flag = 0 #شماره اندیس ها در list_of_spaces
    list_of_spaces.reverse() #ex: 3,2,1
    for star in list_of_number_stars: #چاپ ستاره های بالای قطر لوزی
        print(" " * list_of_spaces[flag] +"*" * star) 
        flag+=1


    print("*" * diameter_of_diamond) #چاپ قطر لوزی
    
    flag = 0
    list_of_spaces.reverse() #ex: 1,2,3
    for star in reversed(list_of_number_stars):#چاپ ستاره های پایین قطر لوزی
        print(" " * list_of_spaces[flag] +"*" * star)
        flag+=1
        


diameter_user_input = int(input("Please enter an odd number: "))#قطر لوزی
calc_diamond(diameter_user_input)








##برگرداندن مقسوم علیه های عدد های ورودی
# def divisors(number):
#      list_of_divisor = []

#      for div in range(1, number+1):
#          if number % div == 0:
#              list_of_divisor.append(div)

#      return list_of_divisor
# #پرفکت بودن
# def is_perfect(number):
#     result = False
#     list_of_sum_div = sum(divisors(number)) - number

    
#     if number == list_of_sum_div:
#         result = True

#     print(f"sum of divisors {number} is {list_of_sum_div}")
#     return result

# print(is_perfect(1000))




##return lenght maximum string & maximum string
# def max_len_string(*args):

#     max_str = args[0]
#     max_len = len(max_str)

#     for word in args:
#         if len(word) > max_len:
#             max_len = len(word)
#             max_str = word
#     return max_len, max_str

# print(max_len_string("hadis","ahmad","hello good morning","hamid","mohammad sadegh",'ali'))