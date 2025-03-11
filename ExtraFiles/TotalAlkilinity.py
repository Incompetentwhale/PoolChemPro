class TotalAlkilinity:
    def __init__(self, totalAlkilinity=80):
        self.totalAlkilinity = totalAlkilinity

    def out_of_bounds(self):
        if self.totalAlkilinity < 80 or self.totalAlkilinity > 120:
            print("Total Alkilinity is out of bounds")

    def get_totalAlkilinity(self):
        return self.totalAlkilinity

    def set_totalAlkilinity(self, totalAlkilinity):
        self.totalAlkilinity = totalAlkilinity
        self.out_of_bounds()

    