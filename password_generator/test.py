for i in list_of_options:
    
    length_pass_user = input(f"Enter length of password: [*enter-> option = {input_defult['lenght']}] ") or input_defult["lenght"]
    print('-'*40, "\nEnter 'Yes' or 'No' to answer the questions.\n", '-'*40)

    upper_case_user = (input(f"Do you want to use 'upper case' in the password? [*enter-> option = {input_defult['y']}] ")).lower() or input_defult['y']
    lower_case_user = (input(f"Do you want to use 'lower case' in the password? [*enter-> option = {input_defult['y']}] ")).lower() or input_defult['y']
    symbol_user = (input(f"Do you want to use 'symbol' in the password? [*enter-> option = {input_defult['y']}] ")).lower() or input_defult['y']
    number_user = (input(f"Do you want to use 'number' in the password? [*enter-> option = {input_defult['y']}] ")).lower() or input_defult['y']
    space_user = (input(f"Do you want to use 'space' in the password? [*enter-> option = {input_defult['n']}] ")).lower() or input_defult['n']