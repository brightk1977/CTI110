# Kristopher Bright
# 6/23/2025
# P2LAB1
# Quick maths for a circle

import math

radius = float(input("What is the radius of the circle? "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("The diameter of the circle is", format(diameter, ".1f"))
print("The circumference of the circle is", format(circumference, ".2f"))
print("The area of the circle is", format(area, ".3f"))

