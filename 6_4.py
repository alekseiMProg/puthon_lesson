from itertools import zip_longest


user = open("users.csv", encoding="utf-8")
hobby = open("hobby.csv", encoding="utf-8")
users_hobby = open("users_hobby.txt", "w", encoding="utf-8")
users = (n.replace(",", " ").strip("\n") for n in user.readlines())
hobbies = (h.strip("\n") for h in hobby.readlines())
user.close()
hobby.close()
for us, hob in zip_longest(users, hobbies):
    users_hobby.writelines(f"{us}: {hob}\n")
users_hobby.close()