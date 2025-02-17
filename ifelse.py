def  calculate_bmi(weight,height):
    bmi = weight/(height*height)
    if bmi < 18.5:
        classification = "underweight"
    elif 18.5 <= bmi <25:
        classification = "normal weight"
    elif 25 <= bmi < 30:
        classification = "over weight"
    else:
        classification = "obese"
    return  f"Your BMI is {bmi:.2f}, which is classified as {classification}"
# print(calculate_bmi(70,1.75))
x = input("Enter your weight in kg: ")
y = input ("Enter your height in meters: ")
print (calculate_bmi(float(x),float(y)))

    
