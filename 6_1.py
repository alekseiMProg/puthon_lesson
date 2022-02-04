with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    my_list = []
    for line in f:
        split_line = (line.split())
        my_tuple = (split_line[0], split_line[5].replace('"', ""), split_line[6])
        my_list.append(my_tuple)

print(my_list)


