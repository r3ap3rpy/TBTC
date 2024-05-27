x = 0

def test_value():
    assert x

def setup():
    global x
    x = 1

def teardown():
    global x 
    x = 1

test_value.setup = setup
test_value.teardown = teardown
