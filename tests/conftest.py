import pytest 
from testingwork.shapes_class import Rectangle

@pytest.fixture
def my_rectangle():
    return Rectangle(5, 10)

@pytest.fixture
def anohter_rectangle():
    return Rectangle(10, 5)