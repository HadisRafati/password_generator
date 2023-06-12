# alphabet_list = ["b","c","d","f","g",'j','k','l',
# 'm','n','p','q','r','s','t',
# 'v','w','x','y','z']   از لیست استفاده کردمisalpha قبل ازمتد

vowels_list = ['u',"a","e",'i','o',]
user_letter = input("Enter the letter: ")  #اینجا از lower استفاده نکردم چون ممکنه بعدن شکل اصلیه ورودی رو بخوام

if len(user_letter) != 1:
    print("Tol vorodi bishtar az 1 ast")
else:
    if user_letter.isalpha():
        if user_letter.lower() in vowels_list:  #اینجا از lower استفاده کردم چون فقد در این ایف اعمال میشه و خارج از بلاک ها به شکل خودشه
            print("Harf seda dar ast")
        else:
            print("Harf seda dar nist")


    else:
        print("Horof alefba nist")
