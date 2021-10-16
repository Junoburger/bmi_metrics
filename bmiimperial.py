one_kg_in_pounds = 0.453592
one_inch_in_meters = 0.0254
# 2.2046226219


weight = float(input("Please enter weight in pounds: "))
height = float(input("Please enter height in inches: "))
weight_in_kg = weight * one_kg_in_pounds
height_in_meters = height * one_inch_in_meters

BMI = round(weight_in_kg / (height_in_meters * height_in_meters), 10)
print("BMI is:", BMI)
