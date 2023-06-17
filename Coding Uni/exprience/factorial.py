number = int(input("Enter Nmber: "))
numbers_range = range(1 , number+1)
factorial = 1

for x in numbers_range:
    factorial *= x
    
print(factorial)