print (" Welcome to My IMC Calculator")
def IMC():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in cm (ex:179) : "))
    IMC = weight / (height / 100) ** 2
    IMC = round(IMC,2)
    print ("hello that your IMC:", IMC)
    
    if IMC < 18.5: 
        print ("Low weight")
    elif IMC <=24.9: 
        print ("Normal weight")
    elif IMC <=29.9:
        print ("Overweight")
    else :    
        print ("obesity")

IMC()
