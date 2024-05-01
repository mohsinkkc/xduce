import pytest
# from py_test.rectangle import Rectangel
import py_test.rectangle as rectangel

@pytest.fixture
def rec():
    return rectangel.Rectangel(30,40)

def test_area(rec):

    assert rec.area() == 30 * 40

def test_perimeter(rec):

    assert rec.perimeter() == (30 * 2) + (40 * 2)