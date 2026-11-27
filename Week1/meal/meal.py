def main():
    time = convert(input("What time is it? "))

    if 7.000 <= time <= 8.000:
        print("breakfast time")
    if 12.000 <= time <= 13.000:
        print("lunch time")
    if 18.000 <= time <= 19.000:
        print("dinner time")

def convert(time):
    minutes = float(time.rpartition(":")[2]) / 60
    return int(time.rpartition(":")[0]) + minutes

if __name__ == "__main__":
    main()
