info_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(info_list))
print(ord("0"))
print(ord("9"))
i = 0
for element in info_list:
    if len(element) > 1:
        for letters in element:
            if letters == "-" or letters == "+":
                info_list[i] = '"' + element.zfill(3) + '"'
                break
            elif 47 < ord(letters) < 58:
                info_list[i] = '"' + element.zfill(2) + '"'
                break
    elif len(element) <= 1 and 47 < ord(element) < 58:
        info_list[i] = '"' + element.zfill(2) + '"'
    i += 1
print(" ".join(info_list))
print(id(info_list))


