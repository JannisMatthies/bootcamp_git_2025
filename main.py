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

while True:
    main()
    _ = input("Programm Schluss. Drücke Enter!")

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

if __name__ == '__main__':
    main()
