hight = float(input("please enter your hieght in cm"))
weight = float(input("please enter your weight in kg"))

BMI = weight / (hight/100) **2
print("your BMI is:",BMI)

if BMI<=18.4:
    print("you are under weight")
elif BMI<=24.9:
    print("you are healthy")
elif BMI<=29.9:
    print("you are overweight")
else:
    print("you are obese")