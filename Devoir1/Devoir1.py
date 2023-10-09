trajets_train = ["BRU-PAR", "BRU-AMS", "BRU-LON", "BRU-COL", "PAR-BOR", 
                "PAR-LYO", "PAR-FRA", "PAR-LON", "PAR-REN", "AMS-BER", 
                "AMS-COL", "AMS-HAM", "COL-HAM", "COL-FRA", "COL-BER", 
                "LYO-MAR", "LYO-ZUR", "FRA-HAM", "FRA-BER", "FRA-MUN", 
                "FRA-ZUR", "BER-MUN", "BER-HAM", "BER-PRA", "MUN-ZUR", 
                "MIL-LYO", "MIL-ZUR", "LYO-BAR", "BAR-MAR", "BOR-TLS", 
                "TLS-BAR", "TLS-MAR", "LON-BIR", "LON-MAN", "MAN-BIR", 
                "MAN-EDI", "EDI-GLW", "LYO-TLS", "HAM-COP", "PAR-TLS"]
durees_train = [80, 95, 120, 105, 120, 110, 230, 140, 90, 385, 180, 
                300, 215, 60, 280, 110, 240, 280, 275, 200, 235, 255, 
                175, 265, 210, 270, 240, 330, 285, 120, 195, 225, 95, 
                140, 80, 190, 50, 250, 280, 260]
ville_depart = "BRU"
durees_voldirect = [65, 120, 85, 80, 100, 60, 90, 100, 60, 105, 75, 80, 85, 
                85, 100, 90, 80, 65, 90, 95, 100, 75]
sacrifice = 60


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
    for i in N: # Première boucle, initialisation du dictionnaire
        d[i] = [15 + distance(t, p, start, i) + 15, 0]

    start = min(d, key=d.get)
    N.remove(start)
    j = 0
    while N != []:
        for i in N:
            diprime = distance(t, p, start, i) + d[start][0] + 15
            if diprime < d[i][0]:
                d[i][0] = diprime
                d[i][1] = d[start][1] +1

        for i in d:
            print(i, d[i])

        start = min(N, key=lambda x : d[x][0])
        N.remove(start)
        
    return d

 

dijkstra(trajets_train, durees_train, "BRU")