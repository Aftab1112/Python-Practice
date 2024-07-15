import math


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)


Area, Circumference = circle_stats(10)

print(f"Area is {Area} and circumference is {Circumference}")
