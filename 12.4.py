# Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        self.dimensions = kwargs

    def calculate(self):
        if self.shape_type == "circle":
            r = self.dimensions['radius']
            area = 3.14 * r ** 2
            peri = 2 * 3.14 * r
        elif self.shape_type == "square":
            s = self.dimensions['side']
            area = s ** 2
            peri = 4 * s
        else:
            return "Shape not supported"
        return f"Area: {area}, Perimeter: {peri}"

circle = Shape("circle", radius=5)
print(circle.calculate())

square = Shape("square", side=4)
print(square.calculate())

