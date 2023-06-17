number_of_digits = int(input("How many numbers do you want to enter? "))
list_of_numbers = []

for x in range(1, number_of_digits+1):
    list_of_numbers.append(int(input("Enter Number: "))) 


print(max(list_of_numbers))