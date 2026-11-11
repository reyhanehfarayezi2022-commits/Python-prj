import time
class LibraryBook :
    def __init__(self):
        self.title = ""
        self.author = ""
        self.book_id = 0
        self.is_available = ""
        self.borrower = ""
        self.fname = ""
        self.lname = ""
        self.password = ""

    def show_info(self):
        time.sleep(1.5)
        print("===="*3 + "\tInfo\t" + "===="*3)
        time.sleep(1.5)
        print("====================================")
        time.sleep(1.5)
        print(f"\nTitle \t. {self.title}\nAuthor \t. {self.author}\nBorrower \t. {self.borrower}\nBook ID \t. {self.book_id}\nStatus \t. {self.is_available}")
        time.sleep(1.5)
    
    def enter_info(self):
        time.sleep(1.5)
        self.fname = str(input("\n*\tFirst name :\t"))
        self.lname = str(input("\n*\tLast name :\t"))
        self.password = int(input("\n*\tPassword :\t"))
        time.sleep(1.5)
        for i in range(0,5):
            time.sleep(0.5)
            print("==========\t"*9)
        return self.check_info()
        
    def check_info(self):
        time.sleep(1.5)
        fn = str(input("\n*\tenter first name :\t"))
        ln = str(input("\n*\tenter last name :\t"))
        pw = int(input("\n*\tenter password :\t"))
        if (fn == self.fname) and (ln == self.lname) and (pw == self.password):
            time.sleep(1.5)
            print("\n=====\tSuccessful Login\t=====")
            time.sleep(1.5)
            for i in range(0,4):
                print("=-=-\t"*10)
            time.sleep(1.5)
            return self.library()
        else:
            while((fn != self.fname) or (ln != self.lname) or (pw != self.password)):
                time.sleep(1.5)
                print("\n=====\tUnsuccessful Login\t=====")
                time.sleep(1.5)
                return self.check_info()

    def library(self):
        time.sleep(1.5)
        print("||||||| -_ Library _- |||||||")
        time.sleep(1.5)
        print(f"\n{self.show_info()}")
        for i in range (0,3):
            time.sleep(1.5)
            print("=--"*15)
        select = str(input("\n\t*borrow book*\t*exit*\t*check status*\t:"))
        if select == "borrow book":
            time.sleep(1.5)
            return self.borrow_book()
        elif select == "exit":
            time.sleep(1.5)
            return self.exit
        elif select == "check status":
            time.sleep(1.5)
            return self.check_status()
        else:
            time.sleep(1.5)
            print("\n\t***\tinvalid choice.\t***")
            time.sleep(1.5)
            return self.library()

    def check_status(self):
        status_dic = {
            "Status" : self.is_available
        }
        if self.is_available == "unavailable":
            status_dic.setdefault("Borrowed by" , self.borrower)
        time.sleep(2)
        print("==="*10)
        print(f"\n***\t{status_dic}\t***")
        return self.library()
        
    def borrow_book(self):
        time.sleep(1)
        print("=====\t"*10)
        #, title , author , book_id , is_available 
        self.title = str(input("\tTitle : \t"))
        self.author = str(input("\tAuthor : \t"))
        self.book_id = int(input("\t Book ID : \t"))

        if self.book_id > 100 :
            self.is_available = "available"
        elif (self.book_id <= 100) and (self.book_id > 0):
            self.is_available = "unavailable"

            time.sleep(2)
            for i in range(0,5):
                print("===============\t"*10)
            time.sleep(2)

        if self.is_available == "available":
            self.borrower = str(self.fname + " " + self.lname)
            time.sleep(1.5)
            print(self.show_info())
            time.sleep(1.5)
            select = str(input("[\tBack ->\t]\t:"))
            if select == "Back":
                time.sleep(1.5)
                return self.library()
        elif self.is_available == "unavailable":
            time.sleep(1.5)
            print(f"{self.title} - {self.book_id} is unavailable.")
            time.sleep(1.5)
            return self.library()

    def exit():
        print("=--"*10)
        print("\n\t\t -- Done --")
        print("=--"*10)

c1 = LibraryBook()
print(c1.enter_info())