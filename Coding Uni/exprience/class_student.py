# 1
# class Student:
#     def __init__(self, name, family, age,email):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.email = email
    
#     def __str__(self):
#         return f"{self.name} {self.family} {self.age} {self.email}"


# p1 = Student("hadis", "rafati", 19, "hadis@gmail.com")

# print(p1)


x = 20

def my_fanc():
    global x
    x = 35

my_fanc()

print(x)
