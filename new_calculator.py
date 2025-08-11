# simple calculator

def calulator():
    print("welcom to simple calculator!")
    print("available opration (+, -, *, /): ")
    

        # get user input
    try:
        num1 = float(input("enter the first number: " ))
        operation =input("enter the opration(+, -, *, /): ")
        num2 = float(input("enter the second number: "))
       

        #perform the valculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1-num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("error: Division by zero is not allowed")
                return 
            result = num1 / num2
        else:
            print("Invalid opreation. please use +, -, *, or /,")
            return
            
            # Display the result
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        print("Error: please enter valid numbers.")

        # Run the calculator
        calculator()
