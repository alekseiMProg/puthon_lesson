src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [src[i + 1] for num, i in zip(src, range(len(src))) if i < len(src) - 1 and num < src[i + 1]]
print(result)
