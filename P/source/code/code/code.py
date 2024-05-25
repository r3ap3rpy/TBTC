class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return f"a + b = {self.a + self.b}"
    def multiply(self):
        return f"a * b = {self.a * self.b}"
    def truthyness(self):
        return True
    def isyness(self):
        return self.a
    def noness(self):
        return None
    def isinness(self):
        return self.a

if __name__ == '__main__':
    c = Calculator(1,2)
    print(c.sum())
