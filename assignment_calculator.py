# Instructions
# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.


#calculator

#welcome message
print("Hello, welcome to the Marketash calculator!")
print("We can help you perform mathematical operations like addition (+), subtraction (-), multiplication (*), or division (/)")

# Taking user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input ("Enter the operation: (+,-,*,/,): ")

#performing the calculations
if operation == "+":
    result = a+b
    print(f"The sum is {result}")

elif operation == "-":
    result = a-b
    print (f"The difference is {result}")

elif operation == "*":
    result = a*b
    print (f"The product is {result}")

elif operation == "/":
    if b !=0:
        result = a/b
        print (f"The quotient is {result}")
    else:
        print("Error: Division by zero is not allowed!")
