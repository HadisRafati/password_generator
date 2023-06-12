input_word = (input("Enter a word: ")).lower()  #Mom
# اگر مام با حروف از اخر تا اول مام برابر بود پالیندروم است


if input_word == input_word[:: -1]:
    print("This is Palindrome")
else:
    print("This is not Palindrome")