def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Input from user
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi_result = calculate_bmi(weight, height)
category = classify_bmi(bmi_result)

print(f"Your BMI is: {bmi_result:.2f}")
print(f"Category: {category}")