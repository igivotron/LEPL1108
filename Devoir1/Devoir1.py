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
        d[i] = [distance(t, p, start, i), 1] # liste contenant la distance et le nombre de transfert
    
    start = min(d, key=d.get)
    N.remove(start)

    while N != []:
        for i in N:
            diPrime = distance(t, p, start, i) + d[start][0]
            if diPrime < d[i][0]:
                d[i][0] = diPrime
                d[i][1] = d[start][1] +1     # Non fonctionnel car se décale

            #d[i] = min(d[i], distance(t, p, start, i) + d[start])
        start = min(N ,key=lambda x : d[x][0])
        N.remove(start)

    return d

d = dijkstra(trajets, poids, "M")
print(d)