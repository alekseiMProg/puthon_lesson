def thesaurus(*args):
    names_dict = {}
    for val in args:
        names_dict.setdefault(val[:1], [])
        if val not in names_dict:
            names_dict[val[:1]].append(val)
    print(names_dict)




thesaurus(*sorted(["Иван", "Екатерина", "Илья", "Мария", "Николай", "Федор"]))

