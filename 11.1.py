# Write a program that receives an integer an input. If a string is entered instead of an integer, then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied

while True:
    try:
        num = int(input("Enter an integer: "))
        print(f"You entered: {num}")
        break  
    except ValueError:
        print("Error: Please enter a valid integer.")
