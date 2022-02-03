from collections import Counter


with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    total_ip = []
    for line in f:
        split_line = (line.split())
        ip = split_line[0]
        total_ip.append(ip)
# Вариант 1
my_dict = {i: 0 for i in total_ip}
for ip in total_ip:
    my_dict[ip] += 1
for key in my_dict:
    if my_dict[key] == max(my_dict.values()):
        print(key, max(my_dict.values()))
        break

# Вариант 2
print(Counter(total_ip).most_common(1))