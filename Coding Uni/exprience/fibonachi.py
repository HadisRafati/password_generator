user_number = int(input("Enter Number: ")) #10

andis_range = range(user_number)  #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
numbers = [0 , 1]

for andis in andis_range:  
    result = numbers[andis] + numbers[andis + 1]

    if result <= user_number:
        numbers.append(result)
    else:
        break

print(numbers[-1])