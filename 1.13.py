#This program converts bytes into KB, MB and GB
a = float(input("Enter size in bytes:"))
def byte_KB():
    b = a / 1024
    print("KB:", b)

def byte_MB():
    b = a / 1024 ** 2
    print("MB:", b)

def byte_GB():
    b = a / 1024 ** 3
    print("GB:", b)

byte_KB()
byte_MB()
byte_GB()
