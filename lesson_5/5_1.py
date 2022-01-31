from sys import argv


def gener(n):
    for i in range(1, n + 1, 2):
        yield i




nums = gener(int(argv[1]))
print(next(nums))
print(next(nums))
print(next(nums))

