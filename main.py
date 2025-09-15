def main():
    x = float(input("Was ist die erste Zahl?\n"))
    y = float(input("Was ist die zweite Zahl?\n"))

    operator = input("Welchen Operator möchtest du nutzen: ")

    solution = 0

    if operator == "+":
        solution = add(x,y)
    elif operator == "-":
        solution = sub(x,y)
    elif operator == "*":
        solution = mul(x,y)
    elif operator == "/":
        solution = div(x,y)
    else:
        print("Bitte gib einen gültigen operator ein")

    print(f"{x} {operator} {y} = {solution}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def mod(x, y):
    return x % y

def pow(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return x ** 0.5

def fac(x):
    if x < 0:
        raise ValueError("Cannot take the factorial of a negative number.")
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, int(x) + 1):
        result *= i
    return result

if __name__ == '__main__':
    while True:
        main()
        _ = input("\nProgramm Schluss. Drücke Enter!")
