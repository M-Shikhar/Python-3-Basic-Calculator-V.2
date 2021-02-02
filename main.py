# Defining function of basic_calculator
def basic_calculator():
    
    # Intro
    print("------------------------------------------------")
    print("Hello Friend, I will calculate anything you want")
    print("------------------------------------------------")
    
    # Run infinitely unless opton is 9.End
    while 1:
        print("What do you want to do?")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power")
        print("6.Divisibility check")
        print("7.Print Remainder")
        print("8.Print Factorial")
        print("9.End")
        a = input("\nPlease enter your choice number\n")
        
        # Return if user's choice is 9.End
        if a == "9":
            print("End. Thankyou for using this calculator")
            return()
            
        # Checking if inputs are valid float numbers or not if a is not 6, 7 or 8
        if a != "6" and a !="7" and a !="8":
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
                    print("That's not a number")
                    flag = 1
                    
        # Checking if inputs are valid integers or not if a is 6 or 7
        if a == "6" or a == "7":
            flag = 0
            try:
                b = int(input("Enter the First Number (Dividend)\n"))
                c = int(input("Enter the Second Number (Divisor)\n"))
            except:
                print("That's not a number")
                flag = 1
            while flag:
                try:
                    b = int(input("Enter the First Number (Dividend)\n"))
                    c = int(input("Enter the Second Number (Divisor)\n"))
                    flag = 0
                except:
                    print("That's not a number")
                    flag = 1
            
        # Asking user to enter valid 2nd number for division, i.e., other than 0
        while a == "4" and c == 0:
            print("You cannot divide a number by 0")
            c = float(input("Enter the Second Number other than 0\n"))
        while a == "6" and c == 0:
            print("You cannot divide a number by 0")
            c = float(input("Enter the Second Number (Divisor) other than 0\n"))
        while a == "7" and c == 0:
            print("You cannot divide a number by 0")
            c = float(input("Enter the Second Number (Divisor) other than 0\n"))
            
        # Addition
        if a == "1":
            print("The Result is",b+c,"!")
            
        # Subtraction
        elif a == "2":
            print("The Result is",b-c,"!")
            
        # Multiplication
        elif a == "3":
            print("The Result is",b*c,"!")
            
        # Division
        elif a == "4":
            print("The Result is",b/c,"!")
            
        # Power
        elif a == "5":
            print("The Result is",b**c,"!")
            
        # Divisibility check
        elif a == "6":
            if b % c == 0:
                print("Divisible!")
            elif b % c != 0:
                print("Not Divisible!")
        
        # Print Remainder
        elif a == "7":
            print("The Result is",b%c,"!")
        
        # Print Factorial
        elif a == "8":
            try:
                b = int(input("Enter the Number whose Factorial is to be found\n"))
            except:
                print("That's not a valid integer")
                flag = 1
            while flag:
                try:
                    b = int(input("Enter the Number whose Factorial is to be found\n"))
                    flag = 0
                except:
                    print("That's not a valid integer")
                    flag = 1
            n = 0
            f = 0
            while n != b:
                f = f+n
                n = n+1
            print("The Result is",f+b,"!")
            
        # Invalid option
        else:
            print("That's not a valid option")
            
# Calling calculator function
basic_calculator()
