number_of_list = list(range(10))
even_list = []

# for x in number_of_list:
#     if (x % 2 == 0):
#         even_list.append(x)
# print(even_list)

even_list = (x for x in number_of_list if x % 2 == 0)

for x in even_list:
    print(x)