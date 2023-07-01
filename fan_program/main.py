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
print("Speed:", speed_1.get_speed())


# set the properties for fan 2
# create instances of the classes for fan 2
# display fan 2