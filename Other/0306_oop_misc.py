
"""
Created on Mar 6, 2023
@Author: Hammond Liu
"""

# Reference: https://www.programiz.com/python-programming/inheritance

class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {i+1}: ")) for i in range(self.n)]
        self.dispSides()

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

    def _hidden(self):
        print('I\'m weakly hidden')     # can be inherited

    def __hidden(self):
        print('I\'m strongly hidden')   # can't be inherited

class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by 
    # calling the __init__ method of the Polygon class
    def __init__(self):
        super().__init__(3)
        self._ttt = 123                 # weakly hidden

    # property decorator (optional)
    @property
    def ttt(self):
        return self._ttt

    # staticmethod decorator (optional)
    @staticmethod
    def work(a, b):
        return a + b

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Calculating and printing the area of the triangle
t.findArea()

# test data hiding
t._hidden()
# t.__hidden()    # error

# test decorators
print(t.ttt)
# print(t.ttt())  # error
print(t.work(3, 5))