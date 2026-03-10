def bmi():
    w=float(input("Enter your Weight (kg) : "))
    h=float(input("Enter your Height (m) : "))
    h=h/100
    bmi=w/(h*h)
    BMI='%.2f'%bmi

    print(f"Your Body mass Index is : {BMI}")
    if bmi>0:
        if bmi<=16:
            print("Below underweight..!")
        elif bmi<=18.5:
            print("Underweight")
        elif bmi<=25:
            print("Healthy..")
        elif bmi<=30:
            print("Overweight")
        else:
            print("Obease")
    else:
        print("Enter valid details")
while True:
    bmi()
