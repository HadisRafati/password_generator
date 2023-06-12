list_of_nums = [-2 ,3 ,10 ,10 ,20] #-2  3  10  10  20

list_of_nums.sort()
print("The list is sorted: " ,list_of_nums)

if len(list_of_nums) <= 0: #این ایف چون که بعدش دستورات دیگه هست به درستی کار نمیکنه و فعلا بلد نیستم درستش کنم
    print("sdfd")
    
max_number = list_of_nums[-1] #20
print("Max number:" ,max_number)

min_number = list_of_nums[0] #-2
print("Max number:" ,min_number)

avg = (max_number + min_number) / 2 #9
print("avrage:" ,avg)

list_length = len(list_of_nums)#5
Result = 0


if list_length % 2 ==1:
    odd_index = int((list_length - 1)  / 2)
    middle_list = list_of_nums[odd_index] #10

else:
    even_index = int(list_length / 2)
    middle_list = ((list_of_nums[even_index] + list_of_nums[even_index -1] ) / 2)

if avg > middle_list:
    Result = "Bigger"
elif avg < middle_list:
    Result = "Smaller"
else:
    Result = "Equal"

print(Result)