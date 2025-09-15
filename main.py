last_solution = 0

def main():
    global last_solution
    x = input(f"Was ist die erste Zahl? (Leer lassen für {last_solution})\n")
    if x == "":
        x = last_solution
    else:
        x = float(x)

    y = input(f"Was ist die zweite Zahl? (Leer lassen für {last_solution})\n")
    if y == "":
        y = last_solution
    else:
        y = float(y)

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

if __name__ == '__main__':
    while True:
        main()
        _ = input("\nProgramm Schluss. Drücke Enter!")
