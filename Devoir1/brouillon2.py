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
    Ns_barre = extract_cities(t)
    Ns_barre.remove(start)
    c=0
    d = {}
    for i in Ns_barre:
        d[i] = float("inf")

    while Ns_barre != []:
        l = [distance(t, p, start, Ns_barre[i]) for i in range(len(Ns_barre))]
        for i in range(len(Ns_barre)):
            d[Ns_barre[i]] = min(d[Ns_barre[i]], l[i] + c)
        dv = min(l)
        v = Ns_barre[l.index(dv)]
        c += dv # Cause des erreurs car se se réénitialise pas si on change de branche
        Ns_barre.remove(v)
        start = v

    return d






print(dijkstra(trajets, poids, "S"))
