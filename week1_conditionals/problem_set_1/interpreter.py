def main():
    expression = input("Input expression as 'num operator num': ").split()
    firstNum = float(expression[0])
    operator = expression[1]
    secondNum = float(expression[2])

    if operator == "+":
        print(firstNum + secondNum)
    elif operator == "-":
        print(firstNum - secondNum)
    elif operator == "x" or operator == "*":
        print(firstNum * secondNum)
    elif operator == "/":
        print(firstNum / secondNum)
    else:
        print("Invalid format")


main()
