class Car:
    def __init__(self, make, model, year, millage):
        self.make = make
        self.model = model
        self.year = year
        self.millage = millage

    def log_trip(self, length_of_trip):
        self.millage += length_of_trip

    def __str__(self):
        return f"This is a {self.make} {self.model} made in {self.year} with {self.millage} miles on it."

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __add__(self, other):
        return self.millage + other.millage

    def __eq__(self, other):
        return self.make is other.make and self.model is other.model and self.year is other.year
