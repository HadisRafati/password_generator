user_price = int(input("Enter a price: "))

if user_price >= 1000:
    print("Too expensive")
elif 500 <= user_price < 1000:
    print("It is expensive")
elif user_price >= 100 and user_price < 500:
    print("It is normal")
elif 0 <= user_price < 100:
    print("It is cheap")
else:
    print("Price cannot be a negative number")