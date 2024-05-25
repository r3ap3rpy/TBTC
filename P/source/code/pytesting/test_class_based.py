class TestClass:
    def test_one(self):
        x = "demo"
        assert x == "demo"

    def test_calculation(self):
        a = 10
        b = 20
        assert a + b == 30


class TestAnotherClass:
    value = 1
    def test_one(self):
        self.value = 2
        assert self.value == 2

    def test_another(self):
        assert self.value == 1
