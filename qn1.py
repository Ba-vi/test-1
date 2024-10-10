#question 1 (a)
# create a python program that calculates the area of atriangle.

def areaOfTriangle():
    base = float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    area=1/2*base*height
    print(f"The area of the triangle with base {base} and height {height} is : {area}.")
areaOfTriangle()