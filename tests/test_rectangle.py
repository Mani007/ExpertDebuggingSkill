import pytest 
from testingwork.shapes_class import Rectangle



def test_rectangle_area(my_rectangle):
    assert my_rectangle.calculate_area() == 50
    
def test_rectangle_perimeter(my_rectangle):
    assert my_rectangle.calculate_perimeter() == 30

def test_equal_to_rectangle(my_rectangle,anohter_rectangle):
    assert my_rectangle != anohter_rectangle
