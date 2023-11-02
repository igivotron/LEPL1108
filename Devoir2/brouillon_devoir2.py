import numpy as np
import time


def addCayley(x, y):
    if (x == "0" and y == "1") or (x == "1" and y == "0"):
        return "1"
    return "0"


def add(x, y):
    z = ""
    for i in range(len(x)):
        z += addCayley(x[i], y[i])
    return z

def transformToBinary(x):
    for i in range(len(x)):
        if x[i] % 2 == 0:
            x[i] = 0
        else:
            x[i] = 1
    return x
def multiply(x, y, pol):
    polX = np.array([int(i) for i in x])
    polY = np.array([int(i) for i in y])
    polC = np.array([int(i) for i in pol])
    mult = transformToBinary(np.polymul(polX, polY))
    mod = transformToBinary(np.polydiv(mult, polC)[1])

    z = "0"*(8-len(mod))
    for i in mod:
        z+=str(int(i))

    return z


def inverse(x, pol):
    z = "00000001"
    for i in range(7):
        x = multiply(x, x, pol)
        z = multiply(z,x,pol)

    return z


x = "01011000"

pol = "101001101"

inverse(x, pol)