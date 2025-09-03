class calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def pow(x, y):
        return x ** y

    def percent(x, y):
        return (x * y) / 100

    print('WELCOME TO YOURS CALCULATOR PROGRAM- TRY ME :):) \n\n')
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Pow")
    print("6. Percent")


    while True:
        
        choice = input('Please Enter your choice: 1/2/3/4/5/6 : ')   
        if choice == '1':
            print('Your choice is Add')
        elif choice == '2':
            print('Your choice is Subtract')
        elif choice == '3':
            print('Your choice is Multiply')
        elif choice == '4':
            print('Your choice is Divide')
        elif choice == '5':
            print('Your choice is Pow')  
        elif choice == '6':
            print('Your choice is Percent')                  
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == '1':
                print("Result add is :", add(x, y))
            elif choice == '2':
                print("Result substract is :", subtract(x, y))
            elif choice == '3':
                print("Result multiply is :", multiply(x, y))
            elif choice == '4':
                print("Result divide is :", divide(x, y))
            elif choice == '5':
                print("Result pow is :", pow(x,y)) 
            elif choice == '6':
                print("Result percent is :", percent(x,y))
            else:
                print("Invalid input.")
        except ValueError:
                print("Please enter a valid number.")
