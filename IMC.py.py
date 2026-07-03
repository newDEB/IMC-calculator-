print (" Welcome to My IMC Calculator")
def IMC():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in cm (ex:179) : "))
    IMC = weight / (height / 100) ** 2
    print ("hello that your IMC:", IMC)
IMC()