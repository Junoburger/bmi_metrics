weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))


BMI = round(weight / (height * height), 2)
print(BMI)
if BMI < 18.5:
    status = "Underweight"
elif BMI > 18.5 and BMI <= 24.9:
    status = "Normal"
elif BMI >= 25 and BMI <= 29.9:
    status = "Overweight"
elif BMI >= 30.0:
    status = "Obese"

else:
    status = "Unknown outcome"

print("BMI is:", BMI, "Status is", status)
