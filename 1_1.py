duration = int(input("Введите количество секунд: "))

sec = duration % 60
min = duration // 60
hour = min // 60
day = hour // 24
min -= hour * 60
hour -= day * 24

print(day, "дн", hour, "час", min, "мин", sec, "сек" )