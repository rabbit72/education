from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lst):
        self.lst = deepcopy(lst)

    def __str__(self):
        temp_res = []
        for n in self.lst:
            temp_res.append('\t'.join(map(str, n)))
        res = '\n'.join(temp_res)
        return res

    def size(self):
        return len(self.lst), len(self.lst[0])


#  exec(stdin.read())
