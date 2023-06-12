user_word = input("Enter the word: ") #h,a,d,i

odd_len = int((len(user_word) -1 ) / 2) #1 = a

if len(user_word) == 0:
    print("Khali")

else:
    if len(user_word) % 2 == 1:
        print(user_word[odd_len])
    else:
        print(user_word [odd_len : odd_len + 2])

    