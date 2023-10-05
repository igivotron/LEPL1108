
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
    for i in range(len(t)):
        if start in t[i] and stop in t[i]:
            return p[i]
    return None

def dijkstra(trajets, poids, start):
    N = extract_cities(trajets)
    Ns = [start]
    N.remove(start)
    m = []
    n = []
    i=0
    for i in range(len(N)):
        n.append(distance(trajets, poids, start, N[i]))


