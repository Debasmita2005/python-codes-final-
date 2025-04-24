# Create a class Weather that has a list containing weather parameters. Define an overloaded in operator that checks whether an item is present in the list. (Hint: define the function __contains__( )in a class.)

class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters


w = Weather(["sunny", "humid", "windy"])
print("humid" in w)   
print("rainy" in w)   
