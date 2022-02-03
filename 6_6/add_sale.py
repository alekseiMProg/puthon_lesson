from sys import argv


with open("bakery.csv", "a", encoding="utf-8") as b:
    # b.write(f"{argv[1]}\n")
    print(f"{argv[1]}", file=b)