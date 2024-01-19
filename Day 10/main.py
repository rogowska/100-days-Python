def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 + n2


if_continue = 'n'

while True:
    if if_continue == 'n':
        n1 = float(input("Whats the first number? "))
    if if_continue == 'y':
        n1 = result
    op = input("Choose the operation: +, -, *, / ")
    n2 = float(input("Whats the second number? "))
    if op == "+":
        result = add(n1, n2)
    if op == "-":
        result = sub(n1, n2)
    if op == "*":
        result = mul(n1, n2)
    if op == "/":
        result = div(n1, n2)
    print(n1, " ", op, " ", n2, " = ", result)
    if_continue = input("Type 'y' to continue operation with " + str(result) + " or 'n' to start new calculator ")
