print("Welcome to Calculator🧮")

while True :
    operation = input("Choose an operation (Add/Subtract/Multiply/Divide) : ").lower().strip()

    if operation not in ["add","subtract","multiply","divide"] :
        print("❌Invalid input")
        continue

    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    if operation == "add" :
        print("Sum is : " , num1 + num2)
    elif operation == "subtract" :
        print("Subtraction is : " , num1 - num2)
    elif operation == "multiply" :
        print("Product is : " , num1 * num2)
    elif operation == "divide" :
        if num2 == 0 :
             print("❌Cannot divide by zero")
        else :
           print("Division is : " , num1 / num2)

    calculate_again = input("Want to calculate again (yes/no)? : ")
    if calculate_again != "yes" :
            print("Thankyou!🙂")
            break