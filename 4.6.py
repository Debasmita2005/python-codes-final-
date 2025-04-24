#This program print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight

def time():
    for i in range(24):
        if i == 0:
            print("12:00 AM - Midnight")
        elif i == 12:
            print("12:00 PM - Noon")
        elif i < 12:
            print(f"{i}:00 AM")
        else:
            print(f"{i - 12}:00 PM")

time()
