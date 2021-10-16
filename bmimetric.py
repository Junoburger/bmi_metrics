weight = float(input("Please enter weight in kilograms: "))
height = float(input("Please enter height in meters: "))

BMI = round(weight / (height * height), 10)
print("BMI is:", BMI)
