def num_tranalate(eng):
    numb_trans = dict(zero="ноль", one="один", two="два", three="три",
                      four="четыре", five="пять", six="шесть", seven="семь",
                      eight="восемь", nine="девять", ten="десять")
    if eng.istitle() == True:
        print(numb_trans.get(eng.lower()).title())
    else:
        print(numb_trans.get(eng))




num_tranalate(input("Please, enter a number from 0 to 10 in Latin: "))