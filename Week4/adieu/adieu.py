import inflect
p = inflect.engine()

song = []

while True:

    try:
        name = input("Name: ")

        song += [name]

    except EOFError:
        break
print(f"\nAdieu, adieu, to {p.join((song))}")