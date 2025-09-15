last_solution = 0

single_operator_operations = ["sqrt", "fac"]


def main():
    global last_solution
    solution = 0
    x = input(f"Was ist die erste Zahl? (Leer lassen für {last_solution})\n")
    if x == "":
        x = last_solution
    else:
        x = float(x)

    operator = input("Welchen Operator möchtest du nutzen: ")

    if operator not in single_operator_operations:
        y = input(f"Was ist die zweite Zahl? (Leer lassen für {last_solution})\n")
        if y == "":
            y = last_solution
        else:
            y = float(y)

        if operator == "+":
            solution = add(x,y)
        elif operator == "-":
            solution = sub(x,y)
        elif operator == "*":
            solution = mul(x,y)
        elif operator == "/":
            solution = div(x,y)
        elif operator == "%":
            solution = mod(x,y)
        elif operator == "^" or operator == "pow" or operator == "**":
            solution = pow(x,y)
        else:
            print("Bitte gib einen gültigen operator ein")

        print(f"{x} {operator} {y} = {solution}")
    else:
        if operator == "sqrt":
            solution = sqrt(x)
        elif operator == "!" or operator == "fac":
            solution = fac(x)
        else:
            print("Bitte gib einen gültigen operator ein")

        print(f"{x} {operator} = {solution}")

    last_solution = solution


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
    print("Hallo, willkommen in diesem Taschenrechner!\n"
          "Es gibt folgende Rechenoperationen:\n"
          "Mit + kannst du addieren.\n"
          "Mit - kannst du subtrahieren.\n"
          "Mit * kannst du multipliezieren.\n"
          "Mit / kannst du dividieren.\n")
    while True:
        main()
        _ = input("\nProgramm Schluss. Drücke Enter!")
