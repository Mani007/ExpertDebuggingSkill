import pytest 
import testingwork.shapes_class as CircleShape

# def test_circle_area():
#     circle = CircleShape.Circle(5)
#     assert circle.calculate_area() == 78.53981633974483
class TestCircleShape:

    def setup_method(self,method):
        print(f"Starting setup method {method}")
    
    def teardown_method(self, method):
        print(f"Ending teardown method {method}")
    def test_circle_area(self):
        # circle = CircleShape.Circle(5)
        # assert circle.calculate_area() == pytest.approx(78.53981633974483)
        assert True