# First task

radius = float(input("Input the radius of the circle: "))
Pi = 3.14
area = Pi * radius * radius
print("The area of the circle with radius 1.1 is:", area)


# Second task

filename = input("Input the Filename:")
file_extns = filename.split(".")
print("The extension of the file is:", repr(file_extns[-1]))

