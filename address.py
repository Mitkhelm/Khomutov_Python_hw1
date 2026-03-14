class Address:
    def __init__(self, index, town, street, house, apartment):
        self.index = index
        self.town = town
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        return f"{self.index}, {self.town}, {self.street}, {self.house} - {self.apartment}"

