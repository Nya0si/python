#prompt user for first nuber
num1 = float(input("Enter the first number: "))

#prompt user for 2nd number
num2 = float(input("Enter the second number: "))

#Request for the operation
operation = input("Enter an operation (+, -, *, /): ")

#Calculate
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} *{num2} = {result}")
elif operation =='/':
    if num2 !=0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please use +, -, *, or /.")