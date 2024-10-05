import math
class Shapes:
    # Abstract class for shapes    
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

# Creating a circle class inheriting from Shapes class
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangle(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    # Equality operator method/function overloading using __eq__ for checking if two given rectangle are equal 
    def __eq__(self, other_rect):
        if not isinstance(other_rect, Rectangle):
            return False
        return self.length == other_rect.length and self.width == other_rect.width
    def calculate_area(self):
        return self.length * self.width
        
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)