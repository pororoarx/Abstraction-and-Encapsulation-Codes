# create a class named Fan
class Fan:
    # set the three constants
    SLOW = 1
    MEDIUM = 2
    FAST =3

    # initialize the properties of the fan
    def __init__(self, speed = SLOW, radius = 5, color = "blue", on = False):
        self.__speed = speed
        self.__radius = radius
        self.__color =  color
        self.__on = on