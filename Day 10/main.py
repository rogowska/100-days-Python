def add(n1, n2):
    result = n1 + n2
    print(n1, " + ", n2, " = ", result)
    return result


def sub(n1, n2):
    result = n1 - n2
    print(n1, " - ", n2, " = ", result)
    return result


def mul(n1, n2):
    result = n1 * n2
    print(n1, " * ", n2, " = ", result)
    return result


def div(n1, n2):
    result = n1 + n2
    print(n1, " / ", n2, " = ", result)
    return result


if_continue = 'n'

while True:
    if if_continue == 'n':
        n1 = int(input("Whats the first number? "))
    if if_continue == 'y':
        n1 = result
    op = input("Choose the operation: +, -, *, / ")
    n2 = int(input("Whats the second number? "))
    if op == "+":
        result = add(n1, n2)
    if op == "-":
        result = sub(n1, n2)
    if op == "*":
        result = mul(n1, n2)
    if op == "/":
        result = div(n1, n2)
    if_continue = input("Type 'y' to continue operation with " + str(result) + " or 'n' to start new calculator ")
