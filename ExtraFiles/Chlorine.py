class Chlorine:
    def __init__(self, chlorine=1):
        self.chlorine = chlorine

    def out_of_bounds(self):
        if self.chlorine < 1 or self.chlorine > 5:
            print("Chlorine is out of bounds")

    def get_chlorine(self):
        return self.chlorine

    def set_chlorine(self, chlorine):
        self.chlorine = chlorine
        self.out_of_bounds()