class Matrix:

    def __init__(self, l):
        self.l = l

    def __str__(self):
        s_1 = self.l[0]
        s = ""
        for i in self.l:
            s += "\n"
            if len(i) == len(s_1):
                for n in i:
                    s += " " + str(n)
            else:
                return f"Количество элементов в списке {self.l} разное. Матрица не может быть создана."
        return s

    def __add__(self, other):
        total_mat = []
        for i in range(len(self.l)):
            new_l = [x + y for x, y in zip(self.l[i], other.l[i])]
            total_mat.append(new_l)
        return Matrix(total_mat)


my_list = [[1, 3], [3, 4], [4]]
mat = Matrix(my_list)
print(mat)
my_list_2 = [[1, 3, 7], [3, 4, 2], [4, 7, 9]]
mat_2 = Matrix(my_list_2)
print(mat_2)
my_list_3 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
mat_3 = Matrix(my_list_3)
print(mat_2 + mat_3)

