import math

def calc_area_of_circle(radius):
    return math.pi * (radius ** 2)

def calc_perimeter_of_circle(radius):
    return 2 * math.pi * radius

def calc_area_of_rectangle(length, width):
    return length * width

def calc_perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def calc_perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

def calc_area_of_triangle(side1, side2, side3):
    semi_perimeter_of_triangle = (side1 + side2 + side3) / 2
    return math.sqrt(semi_perimeter_of_triangle * abs(semi_perimeter_of_triangle - side1) * abs(semi_perimeter_of_triangle - side2) * abs(semi_perimeter_of_triangle - side3))

def main():
    print("Please enter the radius of circle: ")
    radius_of_circle = float(input())

    print("Please enter the length of rectangle: ")
    length_of_rectangle = float(input())

    print("Please enter the width of rectangle: ")
    width_of_rectangle = float(input())

    print("Please enter the length of first side of triangle: ")
    first_side_of_triangle = float(input())

    print("Please enter the length of second side of triangle: ")
    second_side_of_triangle = float(input())

    print("Please enter the length of third side of triangle: ")
    third_side_of_triangle = float(input())

    print(f"Area and Perimeter of Circle of radius: {radius_of_circle:.2f} = {calc_area_of_circle(radius_of_circle):.2f}, {calc_perimeter_of_circle(radius_of_circle):.2f}")
    print(f"Area and Perimeter of Rectangle of length: {length_of_rectangle:.2f} and width: {width_of_rectangle:.2f} = {calc_area_of_rectangle(length_of_rectangle, width_of_rectangle):.2f}, {calc_perimeter_of_rectangle(length_of_rectangle, width_of_rectangle):.2f}")
    print(f"Area and Perimeter of Triangle with side having lengths: {first_side_of_triangle:.2f}, {second_side_of_triangle:.2f} and {third_side_of_triangle:.2f} = {calc_area_of_triangle(first_side_of_triangle, second_side_of_triangle, third_side_of_triangle):.2f}, {calc_perimeter_of_triangle(first_side_of_triangle, second_side_of_triangle, third_side_of_triangle):.2f}")

main()