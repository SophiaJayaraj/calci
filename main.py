print ("Hello World")
print ("This is my github freature branch")
import calci

print("Simple calci ")

a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = calci.add(a, b)

elif operator == "-":
    result = calci.subtract(a, b)

elif operator == "*":
    result = calci.multiply(a, b)

elif operator == "/":
    result = calci.divide(a, b)

else:
    result = "Invalid operator"

print("Result:", result)
