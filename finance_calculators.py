import math

print("investment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan","\n")

# these assign the initial values for the bools for the while loops that comprise the menu. 
# as the calculator is one large while loop, this allows the programe to be repeated indefinitely by the user if they wish to perform multiple calculations
first_menu = False
bond_selected = False
investment_selected = False
compound_selected = False
simple_selected = False
restart_loop = False

# This is the first menu the user sees, and allows navigation to either the bond or investment calculator
# Navigation to the different submenus is achived by toggling the bools that trigger their nested while loops
# The while loop with a nested if-elif-else loop repeats the prompt until either 'investment' or 'bond' is entered by user
# lower() is used to make first_input lowercase before we check if it matches 'investment' or 'bond. entry is thus not case-sensitive
# while looping has been used as the format for the control structure as this is more efficient than a large nested conditional, as python is spared from reading through unused lines to check conditionals
while first_menu == False:     
    calculator_choice = input("Enter either 'investment' or 'bond' to proceed: ")
    calculator_choice = calculator_choice.lower()
    if calculator_choice == "investment":
        print ("You have selected the investment calculator")
        first_menu = True
        investment_selected = True
    elif calculator_choice == "bond":
        print("You have selected the bond calculator")
        first_menu = True
        bond_selected = True
    else:
        print ("Please enter either 'investment' or 'bond'")

    # This is the investment calculator. it will execute if 'investment' was selected at the first menu.
    # While loops and try-except are used to ensure the prompts are repeated until a valid input is given.
    while investment_selected == True:  
        invest_input = False
        while invest_input == False:
            try:
                amount_invested = input("Please enter the amount of money you wish to invest: £")
                amount_invested = float(amount_invested)
                invest_input = True
            except: print("please enter a valid number")
        interest_input = False
        while interest_input == False:
            try:
                interest_rate = input("Please enter the interest rate as a % ")
                interest_rate = float(interest_rate)
                interest_rate = interest_rate / 100.00
                interest_input = True
            except: print("please enter a valid number")
        years_input = False
        while years_input == False:
            try:
                years_invested = input("Please enter the number of years you wish to invest the money: ")
                years_invested = float(years_invested)
                years_input = True
                investment_selected = False
            except: print("please enter a valid number")

        # This is the interest submenu. It allows the user to choose whether compound or simple interest is calculated
        # While loop repeats the input prompt until a valid word is entered
        # valid input toggles the bools that activate either the simple or compound interest calculators
        interest_submenu = False
        while interest_submenu == False:
            print("do you want to calculate simple or compound interest? \nsimple   - calculate simple interest \ncompound - calculate compound interest")
            interest_type = input()
            interest_type = interest_type.lower()
            if interest_type == "simple":
                simple_selected = True
                interest_submenu = True 
            elif interest_type == "compound":
                compound_selected = True
                interest_submenu = True
            else: print("please enter either 'simple' or 'compound'")

    # this displays simple interest calculation when selected at the interest submenu
    while simple_selected == True:
        simple_interest = amount_invested *(1 + interest_rate*years_invested)
        print(f"A £{amount_invested} investment for {years_invested} years at {interest_rate * 100}% simple interest is:\n£{round(simple_interest,2)}" )
        restart_loop = True
        simple_selected = False

    # this displays compound interest calculation when selected at the interest submenu
    while compound_selected == True:
        print("compound interest calculator:")
        compound_interest = amount_invested * math.pow((1+interest_rate),years_invested)
        print(f"A £{amount_invested} investment for {years_invested} years at {interest_rate * 100}% compound interest is:\n£{round(compound_interest,2)}" )
        restart_loop = True
        compound_selected = False
    investment_selected = False


    # This is the bond calculator. it will execute if 'bond' was selected at the first menu. 
    # While loops and try-except are used to repeat prompts until a valid input is given
    while bond_selected == True:
        house_input = False
        while house_input == False:
            try:
                house_value = input ("please enter your house value in pounds: £")
                house_value = float(house_value)
                house_input = True
            except: print("please enter a valid number")
        bond_interest_input = False
        while bond_interest_input == False:
            try: 
                bond_interest = input("please enter the interest rate as a %: ")
                bond_interest = float(bond_interest)
                bond_interest = bond_interest / 100.00
                monthly_interest = bond_interest / 12.00
                bond_interest_input = True
            except: print("please enter a valid number")
        months_input = False
       
        while months_input == False:
            try:
                payment_months = input("please enter the number of months you wish to repay the bond in: ")
                payment_months = float(payment_months)
                months_input = True
            except: 
                print("please enter a valid number")
        bond_repayment = (monthly_interest * house_value)/(1 - (1 + monthly_interest)**(-payment_months))
        print(f"To repay a bond of £{house_value} at {bond_interest * 100} in {payment_months} months, you shall have to pay:\n£{round(bond_repayment,2)} each month.")
        restart_loop = True
        bond_selected = False

        # this executes after either the interest or bond menus
        # it asks the user if they wish to use another function, and then either terminates the program or returns them to the first menu. 
    while restart_loop == True:
        restart_menu = input("would you like to perform another calculation? Y/N: ")
        restart_menu = restart_menu.lower()
        if restart_menu == "y":
            first_menu = False
            restart_loop = False
        elif restart_menu == "n":
            print("Thank you for using the finance calculator!")
            restart_loop = False
        else: print("Please enter either 'Y' or 'N'")