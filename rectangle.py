class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def __iter__(self):
        self.obj = [{"length": self.length}, {"width": self.width}]
        return iter(self.obj)


r = Rectangle(5, 6)

for dimns in r:
    print(dimns)
