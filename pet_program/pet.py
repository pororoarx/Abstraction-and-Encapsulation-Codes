# create Pet class
class Pet:
    def __init__(self, name, animal_type, age):
        # private members
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # setter method for name
    def set_name(self, name):
        self.__name = name

    # setter method for animal type
    def set_anime_type(self, animal_type):
        self.__anime_type = animal_type

    # setter method for age
    def set_age(self, age):
        self.__age = age

    # getter method for name
    # getter method for animal type
    # getter method for age
