user_word = input("enter a word: ")
user_word = user_word.lower()  #had


# word_list = list(user_word)  [h,a,d]
# word_list.reverse()[d,a,h]

#                   ['d','a','h']  ['h','a','d']                                
#    'had'   !=   "dah"                    had
if user_word == ''.join(reversed(list(user_word))):
    print("This is Palindrome")
else:
    print("This is not Palindrome") #چاپ
