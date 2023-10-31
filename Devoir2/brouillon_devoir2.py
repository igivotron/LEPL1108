def addCayley(x, y):
    if (x == "0" and y == "1") or (x == "1" and y == "0"):
        return "1"
    return "0"

def add(x, y):
    z = ""
    for i in range(len(x)):
        z += addCayley(x[i], y[i])
    return z

def multCayley(x, y):
    if x == "1" and y == "1":
        return "1"
    return "0"

def multiply(x, y, pol):
    mult = "00000000"
    while y != "00000000":
        if y[0] == "1":
            mult = add(mult, x)
            y = add(y, "00000001")
        a = a + "0" ### mod pol     x <- (X.x)%P
        y = "0" + y[:-1]            ### y <- y/X

    return mult





x = "10100011"
y = "10110100"
print(add(x,y))



