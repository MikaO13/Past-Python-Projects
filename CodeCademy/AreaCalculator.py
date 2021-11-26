"""
Codecademy - Learn Python
Area Calculator
"""

print("The program is up and running!")

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Enter the radius: "))
  area = (radius ** 2) * 3.14159
  print "The area of the circle with radius {} is {}.".format(str(radius), str(area))
elif option == "T":
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = base * height / 2
  print "The area of the triangle with base {} and height {} is {}".format(str(base), str(height), str(area))
else:
  print "That is not a valid option."
  
print "Exiting program..."