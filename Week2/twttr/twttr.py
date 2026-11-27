def main ():
    print(f"{shorten(input("Input: "))}")


def shorten(word):
    i = 0
    while i <len(word):
        if word[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            word = word[0:i] + word[i+1:len(word)]
            i -= 1
        i += 1
    return word


main()