def welcome():
    print('''
    Welcome to Calculator
    ''')
welcome()
# Define our function
def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    ''')
    n1 = float (input ("Enter your first number: "))
    n2 = float (input ("Enter your second number: "))
    if operation == "+":
        addition = n1 + n2
        print('{:g} + {:g} = '.format(n1, n2))
        print('{:g}'.format(addition))

    elif operation == '-':
        subtraction = n1 - n2
        print('{:g} - {:g} = '.format(n1, n2))
        print('{:g}'.format(subtraction))

    elif operation == '*':
        multiplication = n1 * n2
        print('{:g} * {:g} = '.format(n1, n2))
        print('{:g}'.format(multiplication))

    elif operation == '/':
        try:
            division = n1 / n2
            print('{:g} / {:g} = '.format(n1, n2))
            print('{:g}'.format(division))
        except ZeroDivisionError: 
            print("You can't divide by 0.")
    elif operation == "**":
        power = n1 ** n2
        print("{:g} ** {:g} = ".format(n1, n2))
        print('{:g}'.format(power))
    elif operation == "%":
        modulo = (n1/100) * n2
        print("{:g}% of {:g} = ".format(n1, n2))
        print('{:g}'.format(modulo))

    else:
        print('You have not typed a valid operator, please run the program again.')
    # Call calculate() outside of the function
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later. ♥')
    else:
        again()

try:
    calculate()
    again()
except ValueError: 
    print("Please enter numbers only, run the program again.")

