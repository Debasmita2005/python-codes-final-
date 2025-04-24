#This program converts list of temperature in Fahrenheit degrees to equivalent Celsius degrees
f_temp = list(map(float, input("Enter list of temperatures in Fahrenheit separated by space:").split()))

def fahrenheit_celsius():
    print(f"Temperatures in Fahrenheit:{f_temp}")
    c_temp = [5 / 9 * (i - 32) for i in f_temp]
    print(f"Temperatures in Celsius:{c_temp}")

fahrenheit_celsius()
