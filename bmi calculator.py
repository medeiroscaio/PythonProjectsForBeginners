print("WELCOME TO BMI CALCULATOR")

weight=float(input("Type your weight (kg)  "))
height=float(input("Type your height (m) "))
bmi=weight//height**2

print("Your BMI is {:.2f}".format(bmi))

if bmi < 18.5:
    print("You are underweight")
elif bmi >=18.5 and bmi <25:
    print("You have normal weight")
elif bmi >=25 and bmi <=30:
    print("You are overweight")
elif bmi >30 and bmi <=35:
    print("You are obese")
else:
    print("You are clinically obese")