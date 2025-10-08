class property:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    @property
    def add(self) -> int:
        return self.a+self.b

p = property(2,3)
print(p.add)
print(type(p))
print(type(property))
print(type(type))
help(type)