from Convertation import *


class poly(object):
    """Полином, его 2 представления и арифметические операции в поле по х8 + х7 + х6 + х + 1"""

    def __init__(self, arr):
        # Убираем дубликаты
        a = []
        for i in arr:
            if i not in a:
                a.append(i)
        arr = a
        arr.sort(reverse=True)
        self.vector = ArrToVec(arr)
        self.array = arr
        self.string = ArrToStr(arr)
        self.number = ArrToNum(arr)

    @classmethod
    def fromStr(cls, string):
        return cls(StrToArr(string))

    @classmethod
    def fromVec(cls, vec):
        return cls(VecToArr(vec))

    @classmethod
    def fromNum(cls, num):
        return cls(NumToArr(num))

    def __str__(self):
        return self.string

    def __add__(self, other):
        arr = [a for a in self.array + other.array if (a not in self.array or a not in other.array)]
        return poly(arr)

    def __iadd__(self, other):
        self = self + other
        return self

    def __mul__(self, other):
        p = poly([])
        for i in other.array:
            p += self.shift(i)
        return p.reduce()

    def deg(self):
        if len(self.array) == 0:
            return -666
        else:
            return max(self.array)

    def shift(self, deg):
        arr = [i + deg for i in self.array]
        return poly(arr)

    def reduce(self):
        while self.deg() > 7:
            self += base.shift(self.deg() - 8)
        return self


base = poly.fromStr('x8 + x7 + x6 + x + 1')