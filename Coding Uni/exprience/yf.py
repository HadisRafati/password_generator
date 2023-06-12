

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print((lambda fname , lname: fname + " " + last_name)(first_name , last_name))