num1 = int(input("Enter first nuber"))
num2 = int(input("Enter second number"))
opp = input("input operator")


if opp == "+":
    print(" The addition is", num1 + num2)

elif opp == "-":
    print("The subtraction is", num1 - num2)

elif opp == "/":
    print("The Division is", num1 / num2)

elif opp == "*":
    print("The multiplication is", num1 * num2)

elif opp == "**":
    print("The exponential is",num1 ** num2)
else:
    print("You must enter an arithmetic operator")