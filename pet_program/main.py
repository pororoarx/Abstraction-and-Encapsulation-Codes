# import Pet class
from pet import Pet

# ask user for input: name, animal_type, age
name = input("\nEnter the pet's name: ")
animal_type = input("Enter the type of your pet: ")
age = input("Enter the pet's age: ")

# create instance of the class (Pet)
pet = Pet(name, animal_type, age)

# print inputs of the user
print("\nPet's name:", pet.get_name())
print("Pet's animal type:", pet.get_animal_type())
print("Pet's age", pet.get_age())