class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)


x = Rect(15, 120)
x.area()