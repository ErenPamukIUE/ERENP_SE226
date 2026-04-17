import math

def circle_area(radius):
    return math.pi*(radius**2)

def circle_perimeter(radius):
    return 2*math.pi*radius

def rectangle_area(width,height):
    return width*height

def rectangle_perimeter(width,height):
    return width*2 + height*2

def triangle_area(base,height):
    return base*height/2