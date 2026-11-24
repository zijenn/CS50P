def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(2 <= len(s) <= 6) is False:
        return False
    if s[0:2].isalpha() is False:
        return False

    i = 0
    while i < len(s):
        if s[i] in ['.', ' ', '!', ',']:
                return False
        if s[i].isdigit() is True:
            if s[0:i].isalpha() is True and s[i] == '0':
                return False
            z = i + 1
            while z < len(s):
                if s[z].isalpha() is True:
                    return False
                z += 1
        i += 1

    return True

main ()