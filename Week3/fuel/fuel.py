def main():
    while True:
        try:
            fuel = input("Fraction: ")
            X = int(fuel.partition("/")[0])
            Y = int(fuel.partition("/")[2])

            fuel = X/Y*100

            if X>Y or X<0:
                raise ValueError

        except (ValueError, ZeroDivisionError):
            print("\n")
        else:
            break

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{round(fuel)}%")


main ()