#رمز گشایی

LINE_LENGTH = "-"*15
decryption = []

i = 0
while i == 0:
    user_cryp = input("\nEnter number: ")

    if user_cryp == 'exit':
        break

    decryption.append(chr(int(user_cryp)))
    

print("\n", LINE_LENGTH)
print(f"decryption: {''.join(decryption)}")


#استاد
# my_numbers = '84,113,120,120,123,58,44,117,51,121,44,116,109,112,117,127,44,114,126,123,121,44,112,113,134,114,129,120'
# decryption = []
# for i in my_numbers.split(','):
#     decryption.append(chr(int(i) - 12))


# print('gosha= ',''.join(decryption))