try:

    a = int(input("Enter Your First Number: "))
    b = int(input("Enter Your Second Number: "))

    op = (input("Enter Operator( +, -, *, /)"))

    if op == "+":
        print("Answer =", a+b)

    elif op == "-":
        print("Answer =", a-b)

    elif op == "*":
        print("Answer =", a*b)

    elif op == "/":
        print("Answer =", a/b)

    else:
        print("Invalid Operator")

except ZeroDivisionError:
    print("Error! Cannot Divided by Zero.")
