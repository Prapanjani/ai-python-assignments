class MultipleFunctions():
    def bmi():
        bmi = int(input("Enter the BMI Index:"))
        if(bmi < 18):
            print("Underweight")
        elif(bmi >= 18 and bmi < 25):
            print("Normal")
        elif(bmi >= 25 and bmi < 30):
            print("Overweight")
        else:
            print("Obesity")

    def oddEven():
        num = int(input("Enter a number:"))
        if(num % 2 == 0):
            print(num, "is Even Number")
        else:
            print(num, "is Odd Number")

    def eligibility():
        gender = input("Your Gender:")
        if(gender.lower() =='male'or gender.lower() =='female'):
            age = int(input("Your Age:"))
            if(gender.lower() == 'male'):
                if(age >= 21):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")
            elif(gender.lower() == 'female'):
                if(age >= 18):
                    print("ELIGIBLE")
                else:
                    print("NOT ELIGIBLE")
        else:
            print("Give correct input")

    def percentage():
        sub1 = int(input("Subject1="))
        sub2 = int(input("Subject2="))
        sub3 = int(input("Subject3="))
        sub4 = int(input("Subject4="))
        sub5 = int(input("Subject5="))
        total = sub1 + sub2 + sub3 + sub4 + sub5
        print("Total:", total)
        percentage = (total/500)*100
        print("Percentage:", percentage, "%")

    def area():
        height= int(input("Height:"))
        breadth= int(input("Breadth:"))
        area = (height * breadth) / 2
        print("Area of Triangle:", area)

    def perimeter():
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        perimeter = height1 + height2 + breadth
        print("Perimeter of Triangle:", perimeter)
        