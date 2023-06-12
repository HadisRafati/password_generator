#رمز نگاری

LINE_LENGTH = "-"*15

user_text = input("\nEnter string: ")
print(LINE_LENGTH)

crypto_graphy = []


for char in user_text:
    crypto_graphy.append(str(ord(char) + 12))
    

print(f"Encrypted: {','.join(crypto_graphy)} ")


#استاد
# user_num = "Hello. i'm hadis from dezful"
# decryption = []

# for i in user_num:
#     decryption.append(str(ord(i) + 12))

# print("negary= ",','.join(decryption))