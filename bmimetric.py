

weight = float(input("Please enter weight in kilograms: "))
height_input = float(input("Please enter height in meters: "))
heightNumList = str(height_input).rsplit('.')
height = int("".join(heightNumList))

BMI = weight / (height/100)**2
print("BMI is:", round(BMI, 10))
