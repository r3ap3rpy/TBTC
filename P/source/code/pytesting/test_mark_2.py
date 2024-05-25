from datetime import datetime, timedelta
import pytest

testdata = [
    (datetime(2024,5,25),datetime(2024,5,24),timedelta(1)),
    (datetime(2024,5,24),datetime(2024,5,25),timedelta(-1)),
]

@pytest.mark.parametrize("a,b,expected", testdata)
def test_time_distance(a, b, expected):
    diff = a - b
    assert diff == expected

@pytest.mark.parametrize("a,b,expected", testdata, ids = ["forward","backward"])
def test_time_distance_2(a, b, expected):
    diff = a - b
    assert diff == expected

def idfn(val):
    if isinstance(val, (datetime,)):
        return val.strftime("%Y%m%d")

@pytest.mark.parametrize("a,b,expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected

@pytest.mark.parametrize(
    "a,b,expected",
    [
        pytest.param(
            datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1), id="forward"
        ),
        pytest.param(
            datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1), id="backward"
        ),
    ],
)
def test_timedistance_v3(a, b, expected):
    diff = a - b
    assert diff == expected
