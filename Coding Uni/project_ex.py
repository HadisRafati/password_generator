import matplotlib.pyplot as plt
import numpy as np

class Library:
    
    def __init__(self, user_input, books_dict, reserved ):
        self.user_input = user_input
        self.books_dict = books_dict
        self.reserved = reserved
        

    def menu(self):
    
        if user_input == 1:#add
            pass


        elif user_input == 2:#delet
            isbn_del = int(input("Enter ISBN for Delet book: "))
            for x in books_dict:
                if books_dict[x]["ISBN"] == isbn_del:
                    self.books_dict.pop(x)#*******
                    


        elif user_input == 3:#list
            for x in self.books_dict:
                print(books_dict[x])


        elif user_input == 4:#search
            user_search = input("Enter Name or Auther of book: ")
            for x in self.books_dict:
                if user_search == self.books_dict[x]["name"]:
                    print(self.books_dict[x]["ISBN"])
            
        


        elif user_input == 6:#return
            pass
        elif user_input == 7:#report
            x = np.array([ageGroup])
            

    



####################

class mylib(Library):
    def __init__(self, user_input, books_dict,reserved, res_count):
        super.__init__(user_input, books_dict, reserved)
        self.res_count = res_count

    #l = lambda count : count + 1
    
    def ageOk(self):
        user_age = int(input("Enter your  categori of age: (13 | 18 | 21 | 25)"))
        for x in books_dict:
            if user_age == self.books_dict[x]["ageGroup"]:
                return True

    def reserve(self):
        if self.user_input == 5:#reserve
            user_choose = int(input("Enter ISBN of book: "))
            for x in self.books_dict:
                if self.books_dict[x]["ISBN"] == user_choose:
                    if self.books_dict[x]["status"] == 1:
                        a = self.ageOk()
                        if a == True:
                            print("okkk")
                            self.reserved.append(self.books_dict[x])
                            #l(count = self.res_count)
                            







user_input = int(input("Karet chie: (\n1: add book\n2: Delet Book\n3: List book\n4: search\n5: reserve\n6: return book\n7: report)\n"))

books_dict = {
    "book1" :{
        "ISBN" : 195,
        "name" : "farsi",
        "author" : "vesal",
        "ageGroup" : 18,
        "status" : 1,} ,
        
    "book2" :{
        "ISBN" : 168,
        "name" : "mosh",
        "author" : "ahmad",
        "ageGroup" : 13,
        "status" : 1,},
        }

reserved = []
res_count = 0
x = mylib(user_input, books_dict, reserved, res_count)
x.menu()
x.reserve()
