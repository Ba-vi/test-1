# question2
#using a function create a program that calculates the volume of a cylinder.

def volumeOfCylinder():
    radius =float(input("Enter the radius of a sphere:"))
    height=float(input("Enter the height of the cylinder:"))
    import math
    pie = math.pi
    volume=pie*radius**2*height
    print(f"The volume of a cylinder with radius {radius} and height {height} is : {volume}.")
volumeOfCylinder()
    