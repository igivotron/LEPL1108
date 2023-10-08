trajets = ["S-K", "S-J", "K-J", "K-M", "J-L", "M-L", "L-N"]
poids = [2, 4, 5, 3, 10, 4, 6]


def extract_cities(t):
    cities = []
    for i in t:
        for j in i.split("-"):
            if j not in cities:
                cities.append(j)
    return sorted(cities)

def distance(t, p, start, stop):
    l = []
    if start == stop:
        return 0
    for i in range(len(t)):
        if start in t[i] and stop in t[i]:
            return p[i]
    return float("inf")


def dijkstra(t, p, start):
    N = extract_cities(t)
    N.remove(start)
    d= {}
    for i in N:
        d[i] = distance(t, p, start, i)
    
    start = min(d, key=d.get)
    N.remove(start)

    while N != []:
        for i in N:
            d[i] = min(d[i], distance(t, p, start, i) + d[start])
        start = min(N ,key=lambda x : d[x])
        N.remove(start)

    return d

d = dijkstra(trajets, poids, "M")
print(d)