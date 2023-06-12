user_month_name = (input("Enter a month name: ")).title() #ورودی کاربر کیسش را به تایتل یعنی حرف اول بزرگ تبدیل میکند

seasen_name = ["Bahar" , "Tabestan", "Payiz" , "Zemestan"]

month_name = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar" , "Mehr", "Aban", "Azar" , "Dey", "Bahman", "Esfand"]

result = 0 #برای اینکه چندین بار دستور پرینت را ننویسیم یک متغیر تعریف و در اخر انرا چاپ میکنیم

if user_month_name in month_name:
     if user_month_name in month_name[ : 3]:
          result = seasen_name[0]
     elif user_month_name in month_name[3 : 6]:
          result = seasen_name[1]
     elif user_month_name in month_name[6 : 9]:
          result = seasen_name[2]
     else:
          result = seasen_name[3]
else:
     result = "Invalid input!"


print(result)

#@@@@@#
#پایین کده خودم دست نزدست که با دیکشنری نوشتم

# month_name = {
#     "Bahar" : ["Farvardin", "Ordibehesht", "Khordad"],
#     "Tabestan" : ["Tir", "Mordad", "Shahrivar"],
#     "Payiz" : ["Mehr", "Aban", "Azar"],
#     "Zemestan" : ["Dey", "Bahman", "Esfand"],
# }

# if user_month_name in month_name["Bahar"]:
#     print("Bahar")
# elif user_month_name in month_name["Tabestan"]:
#     print("Tabestan")
# elif user_month_name in month_name["Payiz"]:
#     print("Payiz")
# elif user_month_name in month_name["Zemestan"]:
#     print("Zemestan")
# else:
#     print("Invalid input!")