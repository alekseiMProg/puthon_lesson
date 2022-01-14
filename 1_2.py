cube_list = []
all_sum = 0
all_sum_2 = 0
for i in range(1, 1001):
    if i % 2 != 0:
        cube_list.append(i ** 3)
for n in cube_list:
    number = n
    sum_number = 0
    while n > 0:
        end_number = n % 10
        n = n // 10
        sum_number += end_number
    if sum_number % 7 == 0:
        all_sum += number
print(all_sum)

i = 0
for n in cube_list:
    n += 17
    cube_list[i] = n
    i += 1
for n in cube_list:
    number = n
    sum_number = 0
    while n > 0:
        end_number = n % 10
        n = n // 10
        sum_number += end_number
    if sum_number % 7 == 0:
        all_sum_2 += number
print(all_sum_2)


