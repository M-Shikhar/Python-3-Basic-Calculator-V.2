# Defining function of basic_calculator
def basic_calculator():
    
    # Run infinitely unless opton is 6.End
    print("------------------------------------------------")
    print("Hello Friend, I will calculate anything you want")
    print("------------------------------------------------")
    while 1:
        print("What do you want to do?")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power")
        print("6.End")
        
        # Return if user's choice is 6.End
        a = int(input("Please enter your choice number\n"))
        if a == 6:
            print("End. Thankyou for using this calculator")
            return()
            
        # Checking if inputs are valid float numbers or not
        flag = 0
        try:
            b = float(input("Enter the First Number\n"))
            c = float(input("Enter the Second Number\n"))
        except:
            print("That's not a number")
            flag = 1
        while flag:
            try:
                b = float(input("Enter the First Number\n"))
                c = float(input("Enter the Second Number\n"))
                flag = 0
            except:
                print("Those are not numbers")
                flag = 1
            
        # Asking user to enter valid 2nd number for division, i.e., other than 0
        while a == 4 and c == 0:
            print("You cannot divide a number by 0")
            c = float(input("Enter the Second Number other than 0\n"))
            
        # Addition
        if a == 1:
            print("The Result is",b+c,"!")
            
        # Subtraction
        elif a == 2:
            print("The Result is",b-c,"!")
            
        # Multiplication
        elif a == 3:
            print("The Result is",b*c,"!")
            
        # Division
        elif a == 4:
            print("The Result is",b/c,"!")
            
        # Power
        elif a == 5:
            print("The Result is",b**c,"!")
            
        # Invalid option
        else:
            print("That's not a valid option")
            
# Calling calculator function
basic_calculator()
