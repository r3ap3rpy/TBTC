import pytest
import warnings

def apiv1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return True

@pytest.mark.filterwarnings("ignore:api v1")
def test_warnings():
    assert apiv1() == 1

@pytest.mark.xfail
def test_greater():
    assert 10 > 9


@pytest.mark.xfail
def test_equal():
    assert 10 == 10


@pytest.mark.xfail 
def test_less():
    assert 9 < 10

