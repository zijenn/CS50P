def main():

    grocery = {}

    while True:
        try:
            item = input("\n").upper()
            if item in grocery:
                grocery[item] = grocery[item] + 1
            else:
                grocery[item] = 1
        except EOFError:
            for g in sorted(grocery):
                print(f"{grocery[g]} {g}")
            break
main()