# import class from car
from car import Car

# define a function
def show():
    # create an instance of a class and set the car's model and make
    the_car = Car("2023", "Ferrari")

    # print accelerates text
    print("\n\033[32mAccelerates...🚗\033[0m")

    # use a for loop to call the accelerate method five times
    for i in range(5):
        the_car.accelerate()
        # display the current speed
        print("\033[94mCurrent speed:\033[0m", the_car.get_speed())


    # print brakes text
    print("\n\033[31mBrakes...🚗\033[0m")
    # use a for loop to call the brake method five times
    for i in range(5):
        the_car.brake()
        # display the current speed
        print("\033[93mCurrent speed:\033[0m", the_car.get_speed())


# call the function
show()