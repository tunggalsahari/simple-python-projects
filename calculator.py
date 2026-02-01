num1 = int(input("Enter first number: "))
sign = input("Enter the operation: ")
num2 = int(input("Enter second number: "))

try:
    if sign == "*":
        result = num1 * num2
        print(f"The answer is {result}")
    elif sign == "/":
        num1 / num2
        result = print(f"The answer is {result}")
    elif sign == "+":
        result = num1 + num2
        print(f"The answer is {result}")
    elif sign == "-":
        result = num1 - num2
        print(f"The answer is {result}")
    else:
        print("Operation invalid!")
        
except ZeroDivisionError:
        print(f"The answer is 0")
