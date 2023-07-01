# import class from car
from car import Car

# define a function
def show():
    # create an instance of a class and set the car's model and make
    the_car = Car("2023", "Ferrari")

    # print accelerates text
    print("\nAccelerates...")

    # use a for loop to call the accelerate method five times
    for i in range(5):
        the_car.accelerate()
        # display the current speed
        print("Current speed:", the_car.get_speed())


    # print brakes text

    # use a for loop to call the brake method five times
        # display the current speed


# call the function
show()