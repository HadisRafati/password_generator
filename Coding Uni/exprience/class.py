class simple:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def sum(self):
        print(self.x + self.y)
    
    def sub(self):
        print(self.x - self.y)


class complex(simple):

    def __init__(self, x, y,z):
        super().__init__(x, y)
        self.z = z
    def mul(self):
        print(self.x * self.y)

    def div(self):
        print(self.x / self.y)
    
    def pow(self):
        print(self.x ** self.z)
        print(self.y ** self.z)



obj_comp = complex(10, 5,2)

obj_comp.sum()
obj_comp.sub()
obj_comp.mul()
obj_comp.div()
obj_comp.pow()