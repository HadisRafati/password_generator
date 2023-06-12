# alphabet_list = ["b","c","d","f","g",'j','k','l',
# 'm','n','p','q','r','s','t',
# 'v','w','x','y','z']   از لیست استفاده کردمisalpha قبل ازمتد

vowels_list = ['u',"a","e",'i','o',]
user_letter = input("Enter the letter: ")

if len(user_letter) != 1:
    print("Tol vorodi bishtar az 1 ast")
else:
    print("Vorodi dorost ast")
    if user_letter.isalpha():
        print("Horof alefba ast")
        ######
        if user_letter in vowels_list:
            print("Harf seda dar ast")
        else:
            print("Harf seda dar nist")


    else:
        print("Horof alefba nist")
