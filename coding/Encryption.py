#رمز نگاری متن وارد شده

user_input = input("Enter the desired text: ")
list_encry_text = []

for x in list(user_input):

    
    list_encry_text.append(str(ord(x) + 12))

print(', '.join(list_encry_text))


#رمز گشایی متن وارد شده

user_input = input("Enter the cipher text(, ): ")
list_encry_int = ""
user_input.split()

for x in user_input.split(', '):

    list_encry_int += (str(chr(int(x) - 12)))

print(list_encry_int)