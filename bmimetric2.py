weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))


BMI = round(weight / (height * height), 2)

if BMI < 18.5:
    status = "underweight"
elif BMI > 18.5 and BMI <= 24.9:
    status = "normal"
elif BMI >= 25 and BMI <= 29.9:
    status = "overweight"
elif BMI >= 30.0:
    status = "obese"

else:
    status = "Unknown outcome"

print("BMI is: ", BMI, ", status is ", status, sep="")
