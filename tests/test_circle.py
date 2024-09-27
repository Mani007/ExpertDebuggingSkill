import pytest 
import testingwork.shapes_class as CircleShape

def test_circle_area():
    circle = CircleShape.Circle(5)
    assert circle.calculate_area() == 78.53981633974483
