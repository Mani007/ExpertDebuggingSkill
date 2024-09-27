import pytest
import testingwork.firsttest as firsttest
def test_add():
    assert firsttest.adding(2, 3) == 5
    assert firsttest.adding(-1, -2) == -3
    assert firsttest.adding(-1, -4) == -5  
def test_subtracting():
    assert firsttest.subtracting(5, 3) == 2
    assert firsttest.subtracting(-2, -1) == -1
    assert firsttest.subtracting(-2, 1) == -3
def test_dividing():
    assert firsttest.dividing(6, 2) == 3
    assert firsttest.dividing(-6, 2) == -3
    assert firsttest.dividing(6, -2) == -3
    # with pytest.raises(ZeroDivisionError):
    #     firsttest.dividing(6, 0)
    #     firsttest.dividing(0, 6)
    #     firsttest.dividing(-6, 0)
def test_divide_by_zero():
    result = firsttest.dividing(2,0)
    assert result == True