# create class for color
class Color:
    def __init__(self, fan):        
        # private member
        self.__fan = fan

    # getter method
    def get_color(self):
        return self.__fan._color
    
    # setter method
    def set_color(self, color):
        self.__fan._color = color