class pH:
    def __init__(self, ph=7.2):
        self.ph = ph

    def out_of_bounds(self):
        if self.ph < 7.2 or self.ph > 7.8:
            print("pH is out of bounds")
        
    def get_ph(self):
        return self.ph

    def set_ph(self, ph):
        self.ph = ph
        self.out_of_bounds()