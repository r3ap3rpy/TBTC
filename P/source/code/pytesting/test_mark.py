import pytest

@pytest.mark.parametrize("num, output",[(2,8),(3,9),(4,10)])
def test_addition(num, output):
    assert num + 6 == output
