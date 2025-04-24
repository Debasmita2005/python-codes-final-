# Write a program that creates and uses a Time class to perform various time arithmetic operations.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        extra_hours = total_minutes // 60
        total_minutes %= 60
        total_hours = self.hours + other.hours + extra_hours
        return Time(total_hours, total_minutes)

    def display(self):
        print(f"{self.hours}h {self.minutes}m")


t1 = Time(2, 40)
t2 = Time(3, 30)
t3 = t1.add(t2)
t3.display()
