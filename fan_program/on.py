# create class for on properties
class On:
    def __init__(self, fan):       
        # private member
        self.__fan = fan

    # getter method
    def get_on(self):
        return self.__fan._on

    # setter method
    def set_on(self, on):
        self.__fan._on = on