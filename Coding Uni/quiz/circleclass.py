import math
class circle:
    
    def __init__(self, r, p):
        self.r = r
        self.p = p

    def area(self): #مساحت
        return self.p * self.r**2


class mycircle(circle):

    # def __init__(self, r, p):
    #     super().__init__(r, p)   چون چیزی نمیخواد بهش اضافه کنه پس لزومی به تابع سازنده نیست

    def primeter(self):
        return 2 * self.p * self.r

r = int(input("Enter r:"))
x = mycircle(r , math.pi)

print(x.area())
print(x.primeter())