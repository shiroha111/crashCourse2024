class LogicGate:
    def __init__(self, name):
        self.name = name

    def output(self):
        raise NotImplementedError("非逻辑门")


class AndGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)

    def output(self, a, b):
        return a and b


class OrGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)

    def output(self, a, b):
        return a or b


class NotGate(LogicGate):
    def __init__(self, name):
        super().__init__(name)

    def output(self, a):
        return not a


c1 = AndGate("与")
c2 = OrGate('或')
c3 = NotGate('非')

print(c1.output(0, 0))
print(c1.output(0, 1))
print(c1.output(1, 0))
print(c1.output(1, 1))

print(c2.output(0, 0))
print(c2.output(0, 1))
print(c2.output(1, 0))
print(c2.output(1, 1))

print(c3.output(0))
print(c3.output(1))

