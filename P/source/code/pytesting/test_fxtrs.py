import pytest

@pytest.fixture
def input_value():
    input = 36
    return input

def test_div_by_3(input_value):
    assert input_value / 3 == 12

def test_div_by_6(input_value):
    assert input_value % 6 == 0
