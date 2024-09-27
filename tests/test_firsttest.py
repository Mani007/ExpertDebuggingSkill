import pytest
import testingwork.firsttest as firsttest
def test_add():
    assert firsttest.adding(2, 3) == 5
    assert firsttest.adding(-1, -2) == -3