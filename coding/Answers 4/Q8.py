user_month_type =(input("Enter a Shamsi or Miladi: ")).title()

shamsi_first_months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar"]
shamsi_second_months = ["Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand"]

miladi_first_month = ["January", "February", "March", "April", "May", "June"]
miladi_second_months = ["July", "August", "September", "October", "November", "December"]

if user_month_type == "Shamsi":
    user_shamsi_month = (input("Enter a shamsi month: ")).title()

    if user_shamsi_month in shamsi_first_months :   
        print(31)  
    elif user_shamsi_month in shamsi_second_months:
        if user_shamsi_month == "Esfand":
            print(29)
        else:
            print(30)
    else:
        print("Invalid input!")


elif user_month_type == "Miladi":
    user_miladi_month = (input("Enter a miladi month: ")).title()

    if user_miladi_month in miladi_first_month:
        if user_miladi_month == "February":
            print(28)
        else:
            print(31)  
    elif user_miladi_month in miladi_second_months:
        print(30)
    else:
        print("Invalid input!")
else:
    print("Invalid input!")