def main ():
    amount_due = 50
    while amount_due >0:
        print(f"Amount Due: {amount_due}")
        amount_inserted = int(input("Insert coin: "))
        if amount_inserted in [5, 10, 25]:
            amount_due -= amount_inserted

    if amount_due <0:
        print(f"Change Owed: {-amount_due}")

    elif amount_due == 0:
        print(f"Change Owed: {amount_due}")


main ()
