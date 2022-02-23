import re


class Exc(Exception):
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f"{a} must be a str"


float_pattern = re.compile("\d+\.\d+")
my_list = []
b = True
while b:
    try:
        a = input("Enter the number: ")
        if a.isdigit() or float_pattern.findall(a):
            my_list.append(a)
        else:
            raise Exc(a)
    except Exc:
        print(Exc(a))
    if input("Stop? ").lower() == "yes":
        b = False

print(my_list)
