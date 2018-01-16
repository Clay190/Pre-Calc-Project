#Clay Kynor and Courntey Tally
#1.16.18
#distance.py - calculates distance between two points

from math import sqrt

x1 = float(input("Enter x1 "))
y1 = float(input("Enter y1 "))
x2 = float(input("Enter x2 "))
y2 = float(input("Enter y2 "))

print(sqrt((x2-x1)**2 + (y2-y1)**2))