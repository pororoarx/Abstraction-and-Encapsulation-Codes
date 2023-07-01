# create Car class
class Car:
    def __init__(self, year_model, make):
        # private members
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # accelerate method
    def accelerate(self):
        self.__speed += 5

    # brake method
    def brake(self):
        self.__speed -= 5

    # get speed method
    def get_speed(self):
        return self.__speed