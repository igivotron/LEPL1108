class Data:
    def __init__(self):
        pass

    def trajets_train(self):
        return ["BRU-PAR", "BRU-AMS", "BRU-LON", "BRU-COL", "PAR-BOR", 
                "PARLYO", "PAR-FRA", "PAR-LON", "PAR-REN", "AMS-BER", 
                "AMS-COL", "AMS-HAM", "COLHAM", "COL-FRA", "COL-BER", 
                "LYO-MAR", "LYO-ZUR", "FRA-HAM", "FRA-BER", "FRAMUN", 
                "FRA-ZUR", "BER-MUN", "BER-HAM", "BER-PRA", "MUN-ZUR", 
                "MIL-LYO", "MILZUR", "LYO-BAR", "BAR-MAR", "BOR-TLS", 
                "TLS-BAR", "TLS-MAR", "LON-BIR", "LONMAN", "MAN-BIR", 
                "MAN-EDI", "EDI-GLW", "LYO-TLS", "HAM-COP", "PAR-TLS"]
    
    def durees_train(self):
        return [80, 95, 120, 105, 120, 110, 230, 140, 90, 385, 180, 
                300, 215, 60, 280, 110, 240, 280, 275, 200, 235, 255, 
                175, 265, 210, 270, 240, 330, 285, 120, 195, 225, 95, 
                140, 80, 190, 50, 250, 280, 260]
    
    def ville_depart(self):
        return "BRU"

    def durees_voldirect(self):
        return [65, 120, 85, 80, 100, 60, 90, 100, 60, 105, 75, 80, 85, 
                85, 100, 90, 80, 65, 90, 95, 100, 75]
    
    def sacrifice(self):
        return 60

