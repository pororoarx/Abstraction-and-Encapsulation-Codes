# create class for speed
class Speed:
    def __init__(self, fan):       
        # private member
        self.__fan = fan

    # getter method
    def get_speed(self):
        return self.__fan.__speed

    # setter method
    def set_speed(self, speed):
        self.__fan.__speed = speed