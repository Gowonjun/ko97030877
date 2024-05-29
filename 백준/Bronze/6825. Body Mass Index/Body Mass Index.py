w = float(input())
h = float(input())
BMI = w / pow(h, 2)
if BMI > 25 :
    print('Overweight')
elif BMI >= 18.5 and BMI <= 25 :
    print('Normal weight')
else :
    print('Underweight')