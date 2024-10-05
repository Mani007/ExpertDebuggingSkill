import pytest 
from testingwork.shapes_class import Rectangle

@pytest.fixture
def my_rectangle():
    return Rectangle(5, 10)

def test_rectangle_area(my_rectangle):
    assert my_rectangle.calculate_area() == 50
    
def test_rectangle_perimeter(my_rectangle):
    assert my_rectangle.calculate_perimeter() == 30
