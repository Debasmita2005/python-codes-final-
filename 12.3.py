# Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid.

class Solid:
    def __init__(self, shape, **kwargs):
        self.shape = shape
        self.dimensions = kwargs

    def calculate(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            sa = 6 * side ** 2
            vol = side ** 3
        elif self.shape == "sphere":
            r = self.dimensions['radius']
            sa = 4 * 3.14 * r ** 2
            vol = (4/3) * 3.14 * r ** 3
        else:
            return "Shape not supported"
        return f"Surface Area: {sa}, Volume: {vol}"

# Example usage
cube = Solid("cube", side=4)
print(cube.calculate())

sphere = Solid("sphere", radius=3)
print(sphere.calculate())
