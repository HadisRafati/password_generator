list_of_num = [2,10,3,5,9]

list_length = len(list_of_num)
Result = 0

if list_length == 0:
        Result = "The list is empty."
elif list_length % 2 ==1:
    odd_index = int((list_length - 1)  / 2)
    Result = list_of_num[odd_index]
else:
     even_index = int(list_length / 2)
     ave = ((list_of_num[even_index] + list_of_num[even_index -1] ) / 2)
     Result = ave

print(Result)