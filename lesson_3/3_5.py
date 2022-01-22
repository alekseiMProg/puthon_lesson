from random import sample, choice

#Вариант 1
def get_jokes(num):
    """returns a joke collected from three lists"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    res_list = []
    for i in range(num):
        res_list.append(" ".join(sample(nouns, 1) + sample(adverbs, 1) + sample(adjectives, 1)))
    return res_list


print(get_jokes(5))

#Вариант 2
def get_jokes(num, rep=False):
    """returns a joke collected from three lists
    rep: if it is equal to True, then there will be no repetitions"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    res_list = []
    for i in range(num):
        if nouns == [] or adverbs == [] or adjectives == []:
            break
        noun, adv, adj = choice(nouns), choice(adverbs), choice(adjectives)
        res_list.append(" ".join((noun, adv, adj)))
        if rep is True:
            nouns.remove(noun)
            adverbs.remove(adv)
            adjectives.remove(adj)
    return res_list


print(get_jokes(num=55,rep=True))

