import matplotlib.pyplot as plt
import numpy as np


class Library:

    def __init__(self, books,count_book, reserved, res_count ):
        self.books = books 
        self.reserved = reserved
        self.count_book = count_book
        self.res_count = res_count

    

    def reg_book(self):
        self.count_book += 1
        user_ISBN = int(input("Enter the ISBN of the new book: "))
        user_name_book = input("Enter the Name of the new book: ")
        user_author = input("Enter the author of the new book: ")
        user_ageGroup = int(input("Enter the Age Group of the new book (13 | 18 | 21 | 25): "))
        user_status = int(input("Enter the status of the new book(0 : reserved | 1 : Not Reserved): "))
        user_status = True if user_status == 1 else False

        self.books.update({"book"+str(self.count_book) : {"ISBN" : user_ISBN,
        "name" : user_name_book,
        "author" : user_author,
        "ageGroup" : user_ageGroup,
        "status" : user_status,}})
        print("The book adding operation was done successfully.")

    def del_book(self):
        user_ISBN = int(input("Enter the ISBN of the book: "))
        for key in list(self.books):
            if self.books[key]["ISBN"]  == user_ISBN:
                del self.books[key]
                print("The operation to delete the book was done successfully.")

    def list(self):
        for x in self.books:
            print(books[x])

    def reserve(self, user_ISBN):

        for key in list(self.books):
            if self.books[key]["ISBN"]  == user_ISBN:
                if self.books[key]["status"] == True:
                    self.reserved.append(self.books[key]["ISBN"])
                    z = lambda x : x + 1
                    self.res_count =  z(self.res_count)
                    self.books[key]["status"] = False
                    print("The book reservation operation was successfully completed.")
                    

    def return_book(self):
        user_ISBN = int(input("Enter the ISBN of the book you want to return: "))
        for key in list(self.books):
            if self.books[key]["ISBN"]  == user_ISBN:
                if self.books[key]["status"] == False:
                    self.reserved.remove(self.books[key]["ISBN"])
                    z = lambda x : x - 1
                    self.res_count = z(self.res_count)
                    self.books[key]["status"] = True
                    print("The book return operation was completed successfully.")
                    
    def report(self):
        age = []
        for key in list(self.books):
            age.append(self.books[key]["ageGroup"]) 
            
            age13 = age.count(13)

            age18 = age.count(18)

            age21 = age.count(21)
          
            age25 = age.count(25)

        x = np.array(["13", "18", "21", "25"])
        y = np.array([age13, age18, age21, age25])

        plt.bar(x, y)
        plt.show()

    def serach(self):
        list_of_name = []
        list_of_author = []
        
        user_field = input("Enter the field type(name | author):")
        for key in list(self.books):
            list_of_name.append(self.books[key]["name"])
            list_of_name.append(self.books[key]["author"])
        
        if user_field == "name":
            user_keyword = input("Enter the name of the desired book:")
            for key in list(self.books):
                if self.books[key]["name"] == user_keyword:
                    print(self.books[key]["ISBN"])
        elif user_field == "author":
            user_keyword = input("Enter the author of the desired book:")
            for key in list(self.books):
                if self.books[key]["author"] == user_keyword:
                    print(self.books[key]["ISBN"])



class MyLib(Library):

    def __init__(self,books,count_book, reserved, res_count):
        super().__init__(books,count_book, reserved, res_count)

    def age_ok(self, user_ISBN):
        self.user_ISBN = user_ISBN
        user_age = int(input("Enter your age group(13 | 18 | 21 | 25): "))
        for key in list(self.books):
            if self.books[key]["ISBN"]  == self.user_ISBN:
                
                if self.books[key]["ageGroup"] == user_age:
                    return True
                else:
                    return False


    def reserve(self, obj_lib):
        user_ISBN = int(input("Enter the ISBN of the book you want to reserve: "))
        if self.age_ok(user_ISBN) == True:
            obj_lib.reserve(user_ISBN)
        else:
            print("Your age is not suitable for the age group of the book.")
            print("Unsuccessful reservation!")
            
    def menu(self):

        print("Hello")

        i = 0
        while i<1:
            user_menu= int(input("What is your work: \n1: Add book\n2: Delet Book\n3: List book\n4: Search\n5: Reserve\n6: Return book\n7: Report\n8: Exit\n"))

            if user_menu == 1:
                self.reg_book()
            elif user_menu == 2:
                self.del_book()
            elif user_menu == 3:
                self.list()
            elif user_menu == 4:
                self.serach()
            elif user_menu == 5:
                self.reserve(obj_lib)
            elif user_menu == 6:
                self.return_book()
            elif user_menu == 7:
                self.report()
            elif user_menu == 8:
                print("Bye.")
                i += 1


    

books = {
    "book1" :{
        "ISBN" : 195,
        "name" : "farsi",
        "author" : "vesal",
        "ageGroup" : 18,
        "status" : True,},#t = رزرو نشده 

    "book2" :{
        "ISBN" : 168,
        "name" : "mosh",
        "author" : "ahmad",
        "ageGroup" : 13,
        "status" : True,},
    }
count_book = 2
reserved = []
res_count = 0




obj_lib = Library(books, count_book, reserved, res_count)
obj = MyLib(books, count_book,reserved , res_count)


obj.menu()



#Hadis Rafati