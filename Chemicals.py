class Chemicals:
    def __init__(self, length, width, depth):
        self.volume_gal = length * width * depth * 7.48

    # Chlorine adjustment
    def adjust_chlorine(self, current, target):
        diff = target - current
        if diff > 0:
            chemical = "Calcium Hypochlorite (65%)"
            oz_needed = diff * 2 * (self.volume_gal / 10000)
        elif diff < 0:
            chemical = "Sodium Thiosulfate"
            oz_needed = abs(diff) * 2.6 * (self.volume_gal / 10000)
        else:
            chemical, oz_needed = None, 0
        return chemical, round(oz_needed, 2)

    # pH adjustment
    def adjust_pH(self, current, target):
        diff = round(target - current, 2)
        if diff > 0:
            chemical = "Soda Ash"
            oz_needed = (diff / 0.2) * 6 * (self.volume_gal / 10000)
        elif diff < 0:
            chemical = "Muriatic Acid"
            oz_needed = (abs(diff) / 0.2) * 12 * (self.volume_gal / 10000)
        else:
            chemical, oz_needed = None, 0
        return chemical, round(oz_needed, 2)

    # Alkalinity adjustment
    def adjust_alkalinity(self, current, target):
        diff = target - current
        if diff > 0:
            chemical = "Sodium Bicarbonate"
            oz_needed = (diff / 10) * 24 * (self.volume_gal / 10000)
        else:
            chemical, oz_needed = None, 0
        return chemical, round(oz_needed, 2)

    # Calcium Hardness adjustment
    def adjust_calcium_hardness(self, current, target):
        diff = target - current
        if diff > 0:
            chemical = "Calcium Chloride"
            oz_needed = (diff / 10) * 11 * (self.volume_gal / 10000)
        else:
            chemical, oz_needed = None, 0
        return chemical, round(oz_needed, 2)

    # Stabilizer (CYA) adjustment
    def adjust_cya(self, current, target):
        diff = target - current
        if diff > 0:
            chemical = "Cyanuric Acid"
            oz_needed = (diff / 10) * 13 * (self.volume_gal / 10000)
        else:
            chemical, oz_needed = None, 0
        return chemical, round(oz_needed, 2)