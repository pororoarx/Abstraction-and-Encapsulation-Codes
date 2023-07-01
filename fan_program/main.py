# import Fan class and all the properties
from fan import Fan
from speed import Speed
from radius import Radius
from color import Color
from on import On

# set the properties for fan 1
fan_1 = Fan(Fan.FAST, 10, "yellow", True)

# create instances of the classes for fan 1
speed_1 = Speed(fan_1)
radius_1 = Radius(fan_1)
color_1 = Color(fan_1)
on_1 = On(fan_1)

# display fan 1
print("Fan 1")
print("Speed:", speed_1.get_speed())
print("Radius:", radius_1.get_radius())
print("Color:", color_1.get_color())
print("On properties (True- Turn it On, False- Turn it Off):", on_1.get_on())


# set the properties for fan 2
fan_2 = Fan(Fan.FAST, 5, "blue", False)

# create instances of the classes for fan 2
speed_2 = Speed(fan_2)
radius_2 = Radius(fan_2)
color_2 = Color(fan_2)
on_2 = On(fan_2)

# display fan 2
print("\nFan 2")
print("Speed:", speed_2.get_speed())
print("Radius:", radius_2.get_radius())
print("Color:", color_2.get_color())
print("On properties (True- Turn it On, False- Turn it Off):", on_2.get_on())