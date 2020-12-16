from Convertation import *
from Field import *
from Consts import *
from datetime import datetime
from copy import deepcopy
from Block import *


class key(object):
    """Ключи - по 2 блока"""

    def __init__(self, b1=block(), b2=block()):
        self.b1 = b1
        self.b2 = b2

    def __str__(self):
        return str(self.b1) + ' ' + str(self.b2)

    def F(self, gamma):  # ячейка Фестеля
        state = deepcopy(self)
        tmp1 = state.b1.X(gamma).S().L().X(state.b2)
        res = key()
        res.b2 = self.b1
        res.b1 = tmp1
        return res

    def MakeMiniSchedule(self):  # получаем раундовые ключи
        state = deepcopy(self)
        res = [state.b1, state.b2]
        state = state.F(C[0])
        state = state.F(C[1])
        res = res + [state.b1, state.b2]
        return res


def MiniEncrypt(key, mes):
    state = deepcopy(mes)
    schedule = key.MakeMiniSchedule()
    for i in range(3):
        state = state.X(schedule[i])
        state = state.S()
        state = state.L()
    state = state.X(schedule[3])
    return state
