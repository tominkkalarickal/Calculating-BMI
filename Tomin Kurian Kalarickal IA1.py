#problem_1
# Input - Prompt for inputs
height = float(input("Enter height (inches): "))
weight = float(input("Enter weight (pounds): "))

# Processing - Calculate the BMI result:
bmi = weight / (height ** 2) * 703
#convert to metric
weight_kg = weight * 0.453592
height_m = height* 0.0254
#BMI in metric
bmi_metric = weight_kg / (height_m ** 2)

# Output - Display the result
print("BMI =", bmi)
#formatting the output with f string
print(f'BMI value for a person height of (height) and of weight(weight) formatted using the f string is:(BMI)')
print(f'BMI value for a person height of (height_m) and of weight(weight_kg) formatted using the f string is:(BMI_METRIC)')


# using the round function to round the BMI value to 2 decimal
print("BMI =", round(bmi,1))
print("BMI metric =", round(bmi_metric,1))







