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

t = ["S-K", "S-J", "K-J", "K-M", "J-L", "M-L", "L-N"]
p = [2, 4, 5, 3, 10, 4, 6]

sacrifice = 60

class Mappy:
    def __init__(self, trajets, poids):
        self.t = trajets
        self.p = poids

    def extract_cities(self):
        cities = []
        for i in self.t:
            for j in i.split("-"):
                if j not in cities:
                    cities.append(j)
        return sorted(cities)
    
    def distance(self, start, stop):
        if start == stop:
            return 0
        for i in range(len(self.t)):
            if start in self.t[i] and stop in self.t[i]:
                return self.p[i]
        return float("inf")
    
    def dijkstra(self, start):
        N = self.extract_cities()
        N.remove(start)
        d= {}
        for i in N:
            d[i] = [15 + self.distance(start, i) + 15,0]
        
        start = min(d, key=d.get)
        N.remove(start)

        while N != []:
            for i in N:
                diPrime = self.distance(start, i) + d[start][0] +15
                if diPrime < d[i][0]:
                    d[i][0] = diPrime
                    d[i][1] = d[start][1] +1

            start = min(N, key=lambda x : d[x][0])
            N.remove(start)

        return d

carte = Mappy(trajets_train, durees_train)
train = carte.dijkstra(ville_depart)



ville = list(train.keys())
min_distances_train = []
min_distances_avion = []

for i in range(len(ville)):
    min_distances_train.append(train[ville[i]][0])
    min_distances_avion.append(durees_voldirect[i]+180)

count_train = 0
for i in range(len(min_distances_train)):
    if min_distances_avion[i] + sacrifice > min_distances_train[i]:
        count_train +=1

print(ville)
print(min_distances_train)
print(min_distances_avion)
print(count_train)



