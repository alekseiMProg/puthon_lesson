from sys import argv


n = int(argv[1])
gen = (i for i in range(1, n + 1, 2))
print(*gen)