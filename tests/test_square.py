import pytest
from testingwork.shapes_class import Square

# parameterized testing of all the possible area of square shapes
@pytest.mark.parametrize("side_length, expected_area", [(4, 16), (5, 25), (6, 36)])
def test_multiple_square_area(side_length, expected_area):
    assert Square.calculate_area(side_length) == expected_area