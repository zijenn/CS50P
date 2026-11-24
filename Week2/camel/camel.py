def main():
    camelcase = input("camelCase:")
    snakecase = switchtype(camelcase)
    print(f"snake_case: {snakecase}")


def switchtype(camelcase):
    for i in range(len(camelcase)):
        if camelcase[i].isupper() == True:
            camelcase = camelcase[:i]  + '_' + camelcase[i].lower() + camelcase[i+1:]
    return camelcase

main ()