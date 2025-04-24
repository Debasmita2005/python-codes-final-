#This program converts celcius into fahrenheit
def cel_fah():
    C = float(input("Enter temprature in celcius:"))
    F = (9 / 5 * C) + 32
    print("Fahrenheit:", F)
    
cel_fah()
