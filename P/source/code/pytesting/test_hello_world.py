import pytest

def function(x):
    if x == 2:
        raise ValueError("Incorrect value!")

    if x == 4:
        raise ExceptionGroup(
                "Group message", [ValueError(),AttributeError()],
                )
    return x * 3

def test_function():
    assert function(3) == 9

def test_another_way():
    assert function("#") == '###'

def test_extepion():
    with pytest.raises(ValueError):
        function(2)

def test_exception_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        function(4)
    assert excinfo.group_contains(ValueError)
    assert not excinfo.group_contains(SystemExit)
