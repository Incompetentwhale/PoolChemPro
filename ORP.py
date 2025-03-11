class ORP:
    def __init__(self, orp=650):
        self.orp = orp

    def out_of_bounds(self):
        if self.orp < 650:
            print("ORP is out of bounds")
    
    def get_orp(self):
        return self.orp

    def set_orp(self, orp):
        self.orp = orp
        self.out_of_bounds()