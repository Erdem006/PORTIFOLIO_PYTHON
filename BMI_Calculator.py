BMI_type = input("1:KG 2:Pound ")
BMI_type = int(BMI_type)

def BMI_Kilogram(kilogram ,height):
    return kilogram / (height * height)

def BMI_Pound(pound, height):
    return (pound * 703) / (height * height)

if(BMI_type == 1):
    kilogram = int(input("Enter your kilogram: "))
    height = int(input("Enter your height: ")) / 100
    BMI = BMI_Kilogram(kilogram, height)
else:
    height = int(input("Enter your inches: "))
    pound = int(input("Enter your pound: "))
    BMI = BMI_Pound(pound, height)

BMI = round(BMI, 2)
print(BMI)

if(BMI <= 18.5):
    print("Underweight and Minimal risk")
elif(BMI <= 24.9):
    print("Normal Weight and Minimal risk")
elif (BMI <= 29.9):
    print("Overweight and Increased risk")
elif (BMI <= 34.9):
    print("Obese and High risk")
elif (BMI <= 39.9):
    print("Severely Obese and Very High risk")
elif (BMI >= 40):
    print("Morbidy Obese and Extremely High risk")