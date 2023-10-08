
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
                diPrime = self.distance(self.t, self.p, start, i) + d[start][0]
                if diPrime < d[i][0]:
                    d[i][0] = diPrime
                    d[i][1] = d[start][1] +1    
                
            start = min(N ,key=lambda x : d[x][0])
            N.remove(start)

        return d
    