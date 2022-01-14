percent = int(input("Введите кол-во процентов: "))
end = ["", "а", "ов"]

for i in range(percent + 1):
    if i % 10 == 1 and i % 100 != 11:
        print(f"{i} процент{end[0]}")
    elif i % 10 == 2 and i % 100 != 12 \
            or i % 10 == 3 and i % 100 != 13 \
            or i % 10 == 4 and i % 100 != 14:
        print(f"{i} процент{end[1]}")
    else:
        print(f"{i} процент{end[2]}")