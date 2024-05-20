import math

def get_circle_area(radius):
    return math.pi*radius**2

def get_rect_area(width,height):
    return width*height


import calc_area as ca

area= ca.get_circle_area(10)
print(area)

area=ca.get_rect_area(10,20)
print(area)
