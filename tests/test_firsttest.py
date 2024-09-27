import pytest
import testingwork.firsttest as firsttest
def test_add():
    assert firsttest.adding(2, 3) == 5
    assert firsttest.adding(-1, -2) == -3
    assert firsttest.adding(-1, -4) == -3  
def test_subtracting():
    assert firsttest.subtracting(5, 3) == 2
    assert firsttest.subtracting(-2, -1) == -1
    assert firsttest.subtracting(-2, 1) == -3