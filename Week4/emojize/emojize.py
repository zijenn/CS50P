import emoji


def main():
    answer = input("Input: ")
    print(f"Output: ", emoji.emojize(answer, language = 'alias'))

main()
