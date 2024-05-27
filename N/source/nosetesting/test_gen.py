def check_value(a,b):
    assert a + 1 == b


def check_case(a,b):
    assert a.upper() == b

def test_generator():
    yield check_value, 1, 2
    yield check_value, (2,3)

def test_case():
    yield check_case, "demo","DEMO"
    yield check_case, ("daniel","DANIEL")
