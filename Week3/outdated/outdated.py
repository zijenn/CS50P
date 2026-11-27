months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

def main():
    while True:
        try:
            date = input("Date: ")

            if date.find("/") != -1:
                month = int(date.split("/")[0])

                day = int(date.split("/")[1])

                year = int(date.split("/")[2])
                

            else:
                month = date.partition(",")[0].split(" ")[0]

                month = months.index(month)

                day = int(date.partition(",")[0].partition(" ")[2])

                if not 1 <= day <=31:
                    ValueError

                year = int(date.partition(",")[2])

            print(f"{year}-{month}-{day}")

        except ValueError or TypeError or IndexError:
            continue

main()