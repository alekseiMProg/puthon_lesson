post_name = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Вариант 1
for element in post_name:
    name = element.split()
    print(f"Привет {name[len(name) - 1].capitalize()}")
# Вариант 2
i = 0
for val in post_name:
    print(f"Привет {post_name[i][post_name[i].rfind(' ') + 1 :].capitalize()}!")
    i += 1
