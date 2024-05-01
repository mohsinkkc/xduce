import Unit_test.calculation as calculation 
import pytest


def test_add():
    result= calculation.add(2,3)

    assert result == 5

def test_add_string():
    result=calculation.add('mohsin ','kkc')
    assert result == 'mohsin kkc'


def test_div():
    result= calculation.div(20,5)

    assert result == 4


