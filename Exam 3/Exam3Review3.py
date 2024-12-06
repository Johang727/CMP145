class bballPlayer:
    def __init__(self, name, batAVG):
        self.__name = name
        self.__batAVG = batAVG
    def name(self):
        return self.__name
    def batAVG(self):
        return self.__batAVG
    def __str__(self):
        return f"{self.__name} has a batting average of {self.batAVG}"
    def __lt__(self, other):
        return self.batAVG < other.batAVG
