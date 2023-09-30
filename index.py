
# Body Mass Index(BMI) calculator:
weight = float(input ("What is your Weight(KG)?"))
height = float(input ("What is your Height(meter)?"))

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight person."
    elif 18.5 <= bmi < 24.9:
        return "Healthy Weight person."
    elif 25 <= bmi < 29.9:
        return "Overweight person"
    else:
        return "Obese person."
    
bmi = calculate_bmi(weight, height)
bmi_category = interpret_bmi(bmi)
    
print (f"your BMI is {bmi:.2f}")
print (f"you are Classified as {bmi_category}")
