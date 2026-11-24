def main():
    inputs = input("Expression: ")

    x, y, z = inputs.split(" ")

    x = float(x)
    z = float(z)

    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x*z)
        case"/":
            print(x/z)

main()