import re


def email_parse(email_address):
    RE_USERNAME = r"^[A-Za-z\d]+[\w\.]*[A-Za-z\d]+"
    RE_DOMAIN = r"@([A-Za-z\d]+\.+[A-Za-z]+)"
    return {"username": re.findall(RE_USERNAME, email_address)[0], "domain": re.findall(RE_DOMAIN, email_address)[0]}


email = input("Please, enter email: ")
try:
    dict_parse = email_parse(email)
    print(dict_parse)
except IndexError as e:
    print(f"ValueError: wrong email: {email}")
