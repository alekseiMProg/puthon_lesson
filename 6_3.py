from itertools import zip_longest
from collections import defaultdict


with open("users.csv", encoding="utf-8") as user:
    user_list = [n.replace(",", " ").strip("\n") for n in user.readlines()]
with open("hobby.csv", encoding="utf-8") as hobby:
    hobby_list = [h.strip("\n") for h in hobby.readlines()]
my_dict = defaultdict(str)
if len(user_list) < len(hobby_list):
    exit(1)
for us, hob in zip_longest(user_list, hobby_list):
    my_dict[us] = hob

print(my_dict)
