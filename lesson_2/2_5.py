# Задание A
price = [57.8, 46.51, 97, 53, 23.43, 67.34, 55, 56, 23, 5.9]
i = len(price)
for val in price:
    if i > 1:
        print(f"{int(val)} руб {int(round(val % 1 * 100, 2)):02} коп", end = ", ")
    else:
        print(f"{int(val)} руб {int(round(val % 1 * 100, 2)):02} коп")
    i -= 1

#Задание B
price = [57.8, 46.51, 97, 53, 23.43, 67.34, 55, 56, 23, 5.9]
print(id(price))
price.sort()
print(price)
print(id(price))

#Задание C
price = [57.8, 46.51, 97, 53, 23.43, 67.34, 55, 56, 23, 5.9]
price2 = sorted(price, reverse=True)
print(price2)

#Задание D
price = [57.8, 46.51, 97, 53, 23.43, 67.34, 55, 56, 23, 5.9]
price.sort()
print(price[-5:])