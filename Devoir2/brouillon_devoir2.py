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

def multiply2(x, y, pol):
    mult = "0"*8
    while y != "0"*8:
        if y[-1] == "1":
            mult = add(mult, x)
        x += "0"
        if x[0] == "1":
            x = add(x, pol)[1:]
        else:
            x = x[1:]
        y = "0" + y[:-1]
    return mult



def inverse(x, pol):
    z = "00000001"
    for i in range(7):
        x = multiply(x, x, pol)
        z = multiply(z,x,pol)

    return z


def vandermonde(y):
    k = len(y)
    V = np.zeros((k,k))
    for i in range(k):
        V[i][0] = 1
        for j in range(k-1):
            V[i][j+1] = V[i][j] * y[i]
    return V

def gaussian_elimination(y, I):
    V = vandermonde(y)
    Y = np.array([I])
    Z = np.concatenate((V, Y.T), axis=1)
    print(Z)
    k = len(y)

    x = np.zeros(k)
    for i in range(k):
        for j in range(k):
            if i != j:
                r = Z[j, i] / Z[i, i]
                for m in range(k + 1):
                    Z[j, m] = Z[j, m] - r * Z[i, m]
    for i in range(k):
        x[i] = Z[i, k] / Z[i, i]
    return x


x = "11010110"
z = "00101010"
pol = "101001101"

y = [1, 2, 3, 4, 5]
I = [5, 4, 3, 2, 1]


print(multiply(x,z,pol))
print(multiply2(x,z,pol))
