def add(a, b):
    print(a+b)
    return a + b


def subtract(a, b):
    print(a - b)
    return a - b


def multiply(a, b):
    print(a * b)
    return a * b


def divide(a, b):
    print(a / b)
    return a / b


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calc(term):
    if any(op in term for op in {'+', '-', '*', '/'}):
        for character in reversed(term):
            if character == "+" or character == "-":
                next_term = term.rsplit(character, 1)
                print(next_term)
                a = calc(next_term[0])
                b = calc(next_term[1])
                return operations[character](a, b)
        for character in reversed(term):
            if character == "*" or character == "/":
                next_term = term.rsplit(character, 1)
                print(next_term)
                a = calc(next_term[0])
                b = calc(next_term[1])
                return operations[character](a, b)
    else:
        print(term)
        return int(term)





print("Welcome to my calculator!")
math_query = input("What would you like to calculate?\n")

print(calc(math_query))