"""
input details
    input radius, height, slant height
calculate area
calculate cost
tax calculation
    tax find
    add to main
display
"""
from math import pi

def area(h, r, l):
    a1 = 2 * pi * r * h
    a2 = pi * r * l
    a = a1 + a2
    return a

def cost_cal(area):
    c = int(input("Enter the cost of per metre area : "))
    nc = c * area
    return nc

def tax(cost):
    t = 0.18 * cost
    total = cost + t
    return total

def main():
    height = int(input("Enter the height : "))
    radius = int(input("Enter the radius : "))
    slant_height = int(input("Enter the slant height : "))
    a = area(height, radius, slant_height)
    print(f"Area : {a} m^2")
    nc = cost_cal(a)
    print(f"Cost without tax : {nc}")
    total = tax(nc)
    print(f"Net payable amount : {total}")

main()
