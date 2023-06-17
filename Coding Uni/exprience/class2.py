class simple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def sum(self):
        print(self.x + self.y)
    
    def sub(self):
        print(self.x - self.y)


class complex(simple):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def mul(self):
        print(self.x * self.y)

    def div(self):
        print(self.x / self.y)
    
    def pow(self):
        print(self.x ** self.z)
        print(self.y ** self.z)


adj_simp = complex(10, 5, 2)

adj_simp.sum()
adj_simp.sub()
adj_simp.mul()
adj_simp.div()
adj_simp.pow()