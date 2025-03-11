class Temperature:
    def __init__(self, temperature=82):
        self.temperature = temperature

    def out_of_bounds(self):
        if self.temperature != 82:
            print("Temperature is out of bounds")

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.out_of_bounds()