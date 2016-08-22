# 직사각형 방의 면적

SQ_METERS_PER_SQ_FEET = 0.09290304

length_in_feet = float(input("What is the length of the room in feet? "))
width_in_feet = float(input("What is the width of the room in feet? "))

area_in_sq_feet = length_in_feet * width_in_feet
area_in_sq_meters = area_in_sq_feet * SQ_METERS_PER_SQ_FEET

print("You entered dimentions of " + str(length_in_feet) + " feet " +
      "by " + str(width_in_feet) + " feet")
print("The area is")
print(str(area_in_sq_feet) + " square feet")
print(str(area_in_sq_meters) + " square meters")
