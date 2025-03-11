class TDS:
    def __init__(self, tds=1500):
        self.tds = tds

    def out_of_bounds(self):
        if self.tds < 1500 or self.tds > 2000:
            print("TDS is out of bounds")
        
    def get_tds(self):
        return self.tds

    def set_tds(self, tds):
        self.tds = tds
        self.out_of_bounds()
        