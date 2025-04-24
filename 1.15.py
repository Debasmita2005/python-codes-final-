#This program converts fahrenheit into celcius
def fah_cel():
    F = float(input("Enter temprature in fahrenheit:"))
    C = (F - 32) * 5 / 9
    print("Celcius:", C)
    
fah_cel()
