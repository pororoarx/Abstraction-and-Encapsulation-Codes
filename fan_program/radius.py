# create class for radius
class Radius:
    def __init__(self, fan):        
        # private member
        self.__fan = fan

    # getter method
    def get_radius(self):
        return self.__fan._radius

    # setter method
    def set_radius(self, radius):
        self.__fan._radius = radius