def thesaurus_adv(*args):
    names = {}
    for name in args:
        _x = names.setdefault(name[name.rfind(" ") + 1], {name[0]: [name]})
        if _x != {name[0]: [name]}:
            y = names.get(name[name.rfind(" ") + 1]).setdefault(name[0], []).append(name)
    return names




print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
