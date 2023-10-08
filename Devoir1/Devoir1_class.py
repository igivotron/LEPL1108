
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
            d[i] = self.distance(start, i)
        
        start = min(d, key=d.get)
        N.remove(start)

        while N != []:
            for i in N:
                d[i] = min(d[i], self.distance(start, i) + d[start])
            start = min(N ,key=lambda x : d[x])
            N.remove(start)

        return d
    