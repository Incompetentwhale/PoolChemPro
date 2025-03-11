class CalciumHardness:
    def __init__(self, calciumHardness=200):
        self.calciumHardness = calciumHardness

    def out_of_bounds(self):
        if self.calciumHardness < 200 or self.calciumHardness > 400:
            print("Calcium Hardness is out of bounds")

    def get_calciumHardness(self):
        return self.calciumHardness
    
    def set_calciumHardness(self, calciumHardness):
        self.calciumHardness = calciumHardness
        self.out_of_bounds()