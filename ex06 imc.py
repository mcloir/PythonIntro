weight = float(input("Insert your weigth in kg: "))
height = float(input("Insert your height in cm: "))
imc = weight / (height/100)**2
print("Your IMC is: ", imc)
if imc < 18.5:
    print("You have to eat more")
elif imc < 25:
    print("You are a normal person")
else:
    print("You have to exercise more")