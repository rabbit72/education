from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lst):
        self.lst = deepcopy(lst)

    def __str__(self):
        temp_res = []
        for n in self.lst:
            temp_res.append('\t'.join(map(str, n)))
        res = '\n'.join(temp_res)
        return res

    def __add__(self, other):
        if self.size() == other.size():
            res = []
            for i, n in enumerate(self.lst):
                res.append([])
                for j, m in enumerate(n):
                    res[i].append(self.lst[i][j] + other.lst[i][j])
            return Matrix(res)
        else:
            error = MatrixError(self, other)
            raise error

    def __mul__(self, other):
        res = deepcopy(self.lst)
        for i, n in enumerate(self.lst):
            for j, m in enumerate(n):
                res[i][j] = self.lst[i][j] * other
        return Matrix(res)

    __rmul__ = __mul__

    def size(self):
        return len(self.lst), len(self.lst[0])

    def transpose(self):
        self.lst = list(zip(*self.lst))
        return self

    @staticmethod
    def transposed(obj):
        return Matrix(list(zip(*obj.lst)))


exec(stdin.read())
