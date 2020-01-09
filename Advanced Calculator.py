Number_1 = float(input("Enter first number: "))
Operator = input("Enter an operator: ")
Number_2 = float(input("Enter second number: "))

if Operator == "+":
    print(Number_1 + Number_2)
elif Operator == "-":
    print(Number_1 - Number_2)
elif Operator == "*":
    print(Number_1 * Number_2)
elif Operator == "/":
    print(Number_1 / Number_2)
else:
    print("Please enter a valid operator!")
